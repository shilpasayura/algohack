#educator_modules

'''
AlgoHack Genetic Algorithm for University Semaster Planning
Version 0.03 2018
Niranjan Meegammana Shilpasayura.org
'''

import xdb
import random
import tools
import math
import time
import data



min_mods_per_educator=2 # 2 mods pect eductor
    
def crt_educator_modules_table(cursor,drop):
    if (drop):
        sql="DROP TABLE IF EXISTS educator_modules;"
        success, count=xdb.runSQL(cursor, sql)
    
    sql='''CREATE TABLE educator_modules (
	emid	INTEGER PRIMARY KEY AUTOINCREMENT,
	mid	INTEGER,
	eid	INTEGER,
	fitness INTEGER,
	gid INTEGER DEFAULT 0,
	semid INTEGER DEFAULT 0,
	sessions INTEGER DEFAULT 0);
        '''
    success, count=xdb.runSQL(cursor, sql)
    return success

def insert_educator_modules(cursor,n,delay,gid,semid):   
    sql="SELECT * FROM educator_modules LIMIT 1";
    success, count=xdb.runSQL(cursor, sql)
    
    if (count > 0):
        print("educator_modules table: Records exist")
        return False, 0

    
    success, count=False,0 #reset
    # all educators can teach all modules
    # else we have to set gid and semid and educator modules relationship
    
    sql='''SELECT * FROM educators ORDER by fitness DESC''';
    sql=sql.format(semid,gid,semid,gid)
  
    cursor.execute(sql)
    educators = cursor.fetchall()

    sql="SELECT * FROM modules WHERE gid="+ str(gid) + " and semid=" + str(semid) + " ORDER by fitness ASC";  
    cursor.execute(sql)
    modules = cursor.fetchall()
                  
    edu_mid=[]
    edu_fitness=[]
    i=0
    nmods=len(modules)
    neds=len(educators)
    #number of educators = number of modules
    # we assign 3 modules each  
    for educator in educators:
        eid=educator[0]
        picked=0
        #at least one module for an educator
        if (i < nmods): 
                mid=modules[i][0] # default 1-11 : 1-11 if not skip
                rel1=mid,eid # fitness 3
                if rel1 not in edu_mid:
                    edu_mid.append(rel1)
                    edu_fitness.append(4)
                    picked+=1
                else:
                    pass #what

        #second module
        if (i < nmods): 
            mid2=modules[nmods-i-1][0] # pick from last    
            rel2=mid2,eid # fitness 1
            if rel2 not in edu_mid:
                edu_mid.append(rel2)
                edu_fitness.append(3)
            else:
                fails=0
                while (True):
                    mid3=random.randint(1,nmods)
                    rel3=mid3,eid        
                    if rel3 not in edu_mid:
                        edu_mid.append(rel3)
                        edu_fitness.append(2)
                        break
                    if (fails >= (nmods*nmods)): # try 11 x 11 max
                        break
                        print ("failed ", eid, mid, fails)
                        
                    fails+=1

            # anyone gets 3rd module
            fails=0
            while (True):
                mid4=random.randint(1,nmods)
                rel4=mid4,eid        
                if rel4 not in edu_mid:
                    edu_mid.append(rel4)
                    edu_fitness.append(1)
                    break
                if (fails >= (nmods*nmods)): # try 11 x 11 max
                    break
                    print ("failed ", eid, mid, fails)
                        
                fails+=1
                
        i+=1 # increment module
        
    sqls=""
    i=0
    for midmods in edu_mid:
        mid,eid=midmods
        fitness=edu_fitness[i]
        i+=1
        sql='INSERT INTO educator_modules (eid,mid,fitness,gid, semid) VALUES ({}, {}, {},{}, {}'.format(eid, mid, fitness,gid, semid) +');'
        sqls=sqls + sql
        
    success , count=xdb.runSQL_stmts(cursor, sqls,delay)
    return success, count

def crt_improved_educator_modules_table(cursor,drop):
    if (drop):
        sql="DROP TABLE IF EXISTS improved_educator_modules;"
        success, count=xdb.runSQL(cursor, sql)
    
    sql='''CREATE TABLE improved_educator_modules (
	emid	INTEGER PRIMARY KEY AUTOINCREMENT,
	mid	INTEGER,
	eid	INTEGER,
	fitness INTEGER,
        gid INTEGER DEFAULT 0,
	semid INTEGER DEFAULT 0,
	sessions INTEGER DEFAULT 0);
        '''
    success, count=xdb.runSQL(cursor, sql)
    return success


def crt_view_improved_eductor_modules(cursor):
    sql='''SELECT educators.name, modules.name, EM.fitness, EM.gid, EM.semid FROM improved_educator_modules as EM
INNER JOIN educators , modules ON EM.eid= educators.eid 
and EM.mid=modules.mid order by EM.gid, Em.semid, EM.eid, EM.mid, EM.fitness;
    '''
    
    sql="DROP VIEW IF EXISTS improved_educator_modules_V1;"
    success, count=xdb.runSQL(cursor, sql)
    
    vsql="CREATE VIEW IF NOT EXISTS improved_educator_modules_V1 AS " + sql
    success, count=xdb.runSQL(cursor, vsql)
    return success

def disp_educator_modules(cursor, tbl):
    sql='SELECT educators.name, modules.name, EM.fitness, EM.gid, EM.semid, Em.sessions FROM '+ tbl +' as EM '
    sql=sql+'''INNER JOIN educators , modules ON EM.eid= educators.eid 
            and EM.mid=modules.mid order by EM.eid, EM.fitness DESC, EM.mid;'''
    
    cursor.execute(sql)
    educator_modules = cursor.fetchall()
    for em in educator_modules:
        print(em)

    print ('------------------------')
    
    sql='SELECT modules.name, educators.name, EM.fitness, EM.gid, EM.semid, Em.sessions FROM '+ tbl +' as EM '
    sql=sql+'''INNER JOIN educators , modules ON EM.eid= educators.eid 
            and EM.mid=modules.mid order by EM.mid, EM.fitness DESC, EM.eid;
            '''
    cursor.execute(sql)
    educator_modules = cursor.fetchall()
    for em in educator_modules:
        print(em)

def balance_educator_modules(cursor,gid,semid):
    # this algorithm analizes modules allocated to educators and balance them for equal distribution
    
    sql='''SELECT educators.name, modules.name, EM.fitness, EM.eid , EM.mid, EM.gid, Em.semid
            FROM educator_modules as EM  
            INNER JOIN educators , modules ON EM.eid= educators.eid 
            and EM.mid=modules.mid
            WHERE (EM.gid={} and EM.semid={})
            order by EM.gid, Em.semid, EM.eid, EM.fitness DESC, EM.mid;
        '''
    sql=sql.format(gid,semid)
    print(sql)
    
    lect_mods={}
    mod_lects={}
    cursor.execute(sql)
    educator_modules = cursor.fetchall()
    
    for em in educator_modules:
        key=str('{:02}'.format(em[3]))
        tup=(em[4],em[2])
        if (key in lect_mods):
            lect_mods[key].append(tup)
        else:
            lect_mods[key]=[tup]
            #lect_mods[key].mods=[em[4]]
        
        key=str('{:02}'.format(em[4]))
        tup=(em[3],em[2])
        if (key in mod_lects):
            mod_lects[key].append(tup)
        else:
            mod_lects[key]=[tup]
            #mod_lects[key].lects=[em[3]]

    print(lect_mods)
    #print(mod_lects)

    #lect_mods=tools.sort_dict_key(lect_mods)
    #print(lect_mods)

    nlecturers=len(lect_mods)
    min_mods_per_lect=10000
    max_mods_per_lect=0
    
    for key in lect_mods:
        xlen=len(lect_mods[key]) 
        if (xlen < min_mods_per_lect):
            min_mods_per_lect=xlen
        if (xlen > max_mods_per_lect):
            max_mods_per_lect=xlen

    if min_mods_per_lect==max_mods_per_lect:
        print ("equal allocation modules for educator", min_mods_per_lect, ":", max_mods_per_lect, lect_mods)
    else:
        print ("not equal allocation modules for educator", min_mods_per_lect, ":", max_mods_per_lect, lect_mods)
        # reallocare algo more -> less
        #pass    

    ordered_mod_lects=tools.sort_dict_key(mod_lects)
    nmodules=len(ordered_mod_lects)
    min_lects_per_mod=10000
    max_lects_per_mod=0
    
    for key in mod_lects:
        xlen=len(ordered_mod_lects[key]) 
        if (xlen < min_lects_per_mod):
            min_lects_per_mod=xlen
        if (xlen > max_lects_per_mod):
            max_lects_per_mod=xlen
    
    if min_lects_per_mod==max_lects_per_mod:
        print ("equal educator allocation for modules", min_lects_per_mod, ":", max_lects_per_mod, mod_lects)
    else:
        print ("not equal educator allocation for modules", min_lects_per_mod, ":", max_lects_per_mod, mod_lects)
        # reallocare algo more -> less
        #pass

        av_mods_per_lect= math.ceil((nmodules * 3)/ nlecturers)
        mod_lects_by_val_order=tools.sort_dict_val_len(ordered_mod_lects)

        print ("Module Lecturers" , mod_lects_by_val_order)

        modkeys=mod_lects_by_val_order.keys() # get keys
        key_arr=[] # key array of modules_lects
        for key in modkeys:
            key_arr.append(key) # build a key list
            
        nmods=len(key_arr) # modules to handle
        
        for i in range (nmods): 

            keyneed=key_arr[i] # ones in front need educators
            needlen=len(mod_lects_by_val_order[keyneed]) # actual lecturers for this mod

            if (needlen < av_mods_per_lect): # lessor than average , get from last ones

                for j in range(nmods):
                    keyhave=key_arr[nmods-j-1] # because ordered pick last
                    havelen=len(mod_lects_by_val_order[keyhave])
                    m=0
                    
                    while (needlen+1 < havelen): # until equal or less

                        if ((not mod_lects_by_val_order[keyhave][m] in mod_lects_by_val_order[keyneed]) and (mod_lects_by_val_order[keyhave][m][1] !=4)):
                            #print("pop ", i,j, m, mod_lects_by_order[keyhave][m])
                            mod=mod_lects_by_val_order[keyhave].pop(m) # take
                            mod_lects_by_val_order[keyneed].append(mod) # give
                            needlen+=1 # change new number of lects
                            havelen-=1
                        else:
                            if (m < havelen-1):
                                m+=1 # move to next element
                            else:
                                break # skip to prev
                                
    improved_mod_lects=tools.sort_dict_key(mod_lects_by_val_order)
    print("new mod lects", improved_mod_lects)

    # now based on this recreate lecturer modules
    improved_lect_mods={}

    for key in improved_mod_lects:
        nkey=int(key)
        lects=improved_mod_lects[key]
        #print(lects,key,nkey)
        for i in range(len(lects)):
            modkey=lects[i][0]
            fitness=lects[i][1]
            if (modkey not in improved_lect_mods):
               improved_lect_mods[modkey]=[(nkey,fitness)]
            else:
               improved_lect_mods[modkey].append((nkey,fitness))

            
    print("New lect mods", improved_lect_mods)
    
    for lect_mod in improved_lect_mods:
        eid=lect_mod
        
        for mod in improved_lect_mods[lect_mod]:
            print(lect_mod,mod)
            mid=mod[0]
            fitness=mod[1]
            sql='INSERT INTO improved_educator_modules (eid,mid,fitness,gid,semid) VALUES ({}, {}, {},{}, {}'.format(eid, mid, fitness,gid,semid,) +');'
            success, count=xdb.runSQL(cursor, sql)
            time.sleep(0.05)
            pass
    #print ("Lecturer Modules ", lect_mods)
    #print ("Module Lectturers" , mod_lects)
    return True
    
if __name__ == "__main__":

    delay=0.05
    conn=xdb.opendb('genetic56.db')
    cursor =conn.cursor() # create a cursor object

    success=crt_educator_modules_table(cursor,True) # create spaces table
    success, count =insert_educator_modules(cursor,11,delay,1,1) # generate modules
    xdb.commit(conn)
    disp_educator_modules(cursor,"educator_modules")
    success=crt_improved_educator_modules_table(cursor, True)
    success=balance_educator_modules(cursor,1,1)
    xdb.commit(conn)
    success=crt_view_improved_eductor_modules(cursor)
    xdb.commit(conn)
    disp_educator_modules(cursor,"improved_educator_modules")
    xdb.closedb(conn)
    
