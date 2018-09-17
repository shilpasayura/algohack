#semaster_calander

'''
AlgoHack Genetic Algorithm for University Semaster Planning
Version 0.03 2018
Niranjan Meegammana Shilpasayura.org
'''

import xdb
import random
import tools
import time

min_mods_per_educator=2 # 2 mods pect eductor


def disp_semaster_calander(cursor):
    sql='''
    SELECT EC.gid, EC.semid, spaces.name, EC.nweek,  EC.nweekday, EC.nday, EC.sesid, educators.name, modules.name, EC.nlesson, EC.nsession FROM semaster_calander as EC 
INNER JOIN spaces, educators , modules ON EC.spid=spaces.spid and EC.eid= educators.eid 
and EC.mid=modules.mid order by EC.gid, EC.semid, EC.nsession;
    '''

    cursor.execute(sql)
    semaster_calander = cursor.fetchall()
    for em in semaster_calander:
        print(em[0], em[1],em[2], em[3], em[4],em[5],em[6], em[8], em[9],em[10])
    
    
def crt_semaster_calander_table(cursor):

    sql="DROP TABLE IF EXISTS semaster_calander;"
    success, count=xdb.runSQL(cursor, sql)
    
    sql='''CREATE TABLE semaster_calander (
	spclid INTEGER PRIMARY KEY AUTOINCREMENT,
        gid     INTEGER,
        semid   INTEGER,
        spid	INTEGER,
        nsession INTEGER,
        nday INTEGER,
        eid	INTEGER,
        mid	INTEGER,
        nlesson	INTEGER,
        nweek   INTEGER,
        nweekday    INTEGER,
	sesid	INTEGER,
	fitness INTEGER,
	genetics varchar(100),
        status  INTEGER,
	adate	date,
	sptype INTEGER);
      '''
    success, count=xdb.runSQL(cursor, sql)
    return success

def crt_view_semaster_calender(cursor):
    
    sql="DROP VIEW IF EXISTS semaster_calender_V1;"
    success, count=xdb.runSQL(cursor, sql)

    sql='''
    SELECT EC.gid, EC.semid, EC.nsession, EC.nday, EC.nweek, EC.nweekday, EC.sesid, spaces.name, educators.name, modules.name, EC.nlesson FROM semaster_calander as EC 
    INNER JOIN spaces, educators , modules ON EC.spid=spaces.spid and EC.eid= educators.eid 
    and EC.mid=modules.mid order by EC.gid, EC.semid, EC.nsession;
    '''
        
    vsql="CREATE VIEW IF NOT EXISTS semaster_calender_V1 AS " + sql
    success, count=xdb.runSQL(cursor, vsql)
    return success

def pick_space(cursor,sptype, gid, semid, space_hits):
    # select best space by gid, semid and fitness
    # if it has already been selected
    
    sql='''SELECT * FROM  spaces WHERE (sptype={} and gid={} and semid={}) or
    (sptype={} and gid=0 and semid=0) or (sptype={} and (gid=0 or semid=0))
    ORDER by sptype, gid, semid, fitness DESC'''
    sql=sql.format(sptype,gid,semid,sptype, sptype)
    cursor.execute(sql)
    spaces = cursor.fetchall()
    slen=len(spaces)
    if (slen==0):
        return 0
    print(sql)
    spid=spaces[0][0]
    

    return spid

def pick_module_educator(cursor, mid,eid_hits):
    #pick educator by fitness 
    sql="SELECT * FROM improved_educator_modules WHERE mid=" + '{}'.format(mid) +" order by fitness DESC, eid;"
    cursor.execute(sql)
    educators = cursor.fetchall()
    
    elen=len(educators)
    if (elen==0):
        return 0
    eid=educators[0][2]
    
    return eid

def pick_alternative_educator(cursor, mid,no_eid,fails, alt_eid_hits):
    #pick educator by fitness 
 
    sql="SELECT * FROM improved_educator_modules WHERE mid=" + '{}'.format(mid) +' and eid!={}'.format(no_eid) +' order by fitness DESC, eid;'
 
    cursor.execute(sql)
    educators = cursor.fetchall()
    
    if len(educators) == 0:
        return 0

    eid=educators[0][2]
    return eid
        
def book_calender(cursor,gid,semid,spid,sptype,nsession,mid,eid,nlesson,mid_hits,eid_hits,space_hits):
    # is spid, nday, nession, eid taken
    keep_trying=True
    can_book=False
    fails=0
    alt_eid_hits=[eid]
    
    while (keep_trying):
        space_ok=False
        educator_ok=False
        group_ok=False
    
        # is space available
        sql='SELECT * from  semaster_calander WHERE ' + ' (spid={} and nsession={}'.format(spid, nsession) +');'
        cursor.execute(sql)
        space_booked = cursor.fetchall()
    
        if (space_booked==[]): # can book space
            
            space_ok=True
            sql='SELECT * from  semaster_calander WHERE ' + ' (eid={} and nsession={}'.format(eid, nsession) +');'
            cursor.execute(sql)
            educator_booked = cursor.fetchall()
        
            if (educator_booked==[]): # can book space

                educator_ok=True
                sql='SELECT * from  semaster_calander WHERE ' + ' (gid={} and semid={} and nsession={}'.format(gid, semid, nsession) +');'
                cursor.execute(sql)
                group_booked = cursor.fetchall()

                if (group_booked==[]): # can book space
                    group_ok=True
                    keep_trying=False
                else:
                    fails+=1
                    keep_trying=False
            else:
                # pick other educator and try
                eid=educator_booked[0][5]
                eid=pick_alternative_educator(cursor, mid,eid,fails, alt_eid_hits)
                fails+=1
        else:
            # change space and retry
            fails+=1
            keep_trying=False
            
        if (fails > 3):
            keep_trying=False

    #
    
    if  (space_ok and educator_ok and group_ok) :
        can_book=True
    else:
        return False, space_ok, educator_ok, group_ok
    
    nday,nweek,nweekday,sesid=convert_session(nsession)
        
    status=1 # booked
        
    sql='INSERT INTO semaster_calander (gid, semid, spid, sptype, nsession, eid, mid, nlesson, nday, nweek, nweekday, sesid, status) VALUES ('
    sql=sql+ '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(gid, semid, spid, sptype, nsession, eid, mid, nlesson, nday, nweek, nweekday, sesid,status) +');'
    print(sql)
    cursor.execute(sql) 
    return True, space_ok, educator_ok, group_ok

def convert_session(nsession):
    if (nsession % 4==0):
        sesid=4
        nday=(nsession/4)
    else:
        sesid=nsession % 4
        nday=(nsession//4) +1

    if (nsession % 20==0):
        nweek=nsession/20
    else:
        nweek=(nsession//20) +1

    nweekday=nday % 5

    if (nweekday==0):nweekday=5
        
    return nday,nweek,nweekday,sesid


def create_semaster_calander(cursor,delay,gid,semid):   
    sql="SELECT * FROM semaster_calander LIMIT 1";
    success, count=xdb.runSQL(cursor, sql)
    
    if (count > 0):
        print("semaster_calander table: Records exist")
        return False, 0

    success, count=False,0 #reset
    
    
    sql='SELECT * FROM modules WHERE gid={} and semid={} order by fitness'.format(gid,semid);
    cursor.execute(sql)
    modules = cursor.fetchall()
    
    mid_hits=[]
    space_hits=[]
    eid_hits=[]

    nsession=0 # session
    week=0
    last_mod_first_session=0
    last_lab_first_session=2
        
    for mod in modules: # on fitness 1- 11

        
        #name,weeks, lectures, labworks, leclab_gap, gid, semid
        mid=mod[0]
        mod_name=mod[1]
        mod_nweeks=mod[2]
        lect_per_week=mod[3]
        labs_per_week=mod[4]
        mod_fitness=mod[5]
        lectlab_gap=mod[6]
        mod_nlectures=lect_per_week * mod_nweeks 
        mod_nlabs=labs_per_week * mod_nweeks
    
        
        eid=pick_module_educator(cursor, mid,eid_hits) # pick educator best fit

        if (eid == 0): # no educator
            print ("no educator for module ", mid, eid_hits)
            continue
        
        
        lesson=1
        mod_lect_done=False
        mod_lab_done=False
        nsession=last_mod_first_session+1    

        # we first allocate cal for  module lectures
        sptype=1 # lecture
        spid=pick_space(cursor,sptype, gid, semid, space_hits) # pick lecture space
         
        while not mod_lect_done:
            weekdone=False
            fails=0
            while (not weekdone):

                #try first session
                # returns success, space_ok, educator_ok, group_ok
                success,sp,ed,gr=book_calender(cursor,gid,semid,spid,sptype,nsession,mid,eid,lesson,mid_hits,eid_hits,space_hits) # some extra info
              
                if (success):
                    print("Success ", spid,nsession,eid, mid, lesson)

                    if (lesson==1) :
                        last_mod_first_session=nsession  # next lecture after this

                    if (lesson==mod_nlectures): # end for this module lectures
                            mod_lect_done=True
                            break
                    else:
                        lesson+=1
                        if (lect_per_week ==1):
                            weekdone=True
                            nsession+=20 # skip 1 week mean 20 sessions
                        elif (lect_per_week ==2):
                             # do in this week 
                            nsession+=4 # skip 1 day
                else:
                    print("Tried and failed Lecture ", fails, spid,nsession,eid, mid, lesson)
                    if (fails > 100):
                        print("Failed ", fails, spid,nsession,eid, mid, lesson)
                        #last_mod_first_session+=1
                        mod_lect_done=True
                        break
                    else:
                        nsession+=1 # try next session

                if nsession > 300:
                    pass
                    #nsession=280 # skip 1 day
                    
                time.sleep(delay/5)     
            # week
        #mod done

        # work on lab allocation    
        lesson=1
        mod_lab_done=False
        nday,nweek,nweekday,sesid=convert_session(last_mod_first_session)
        
        if sesid ==1:
            nsession=last_mod_first_session+2 # 0
        elif sesid==2:
            nsession=last_mod_first_session+1 # 0
        elif sesid==3:
            nsession=last_mod_first_session+1 # 0
        elif sesid==4:
            nsession=last_mod_first_session+3 # 0
    
        
        sptype=2 # lab
        spid=pick_space(cursor,sptype, gid, semid, space_hits) # pick space

        while not mod_lab_done:
            weekdone=False
            fails=0
            while (not weekdone):

                #try first session
                # returns success, space_ok, educator_ok, group_ok
                success,sp,ed,gr=book_calender(cursor,gid,semid,spid,sptype,nsession,mid,eid,lesson,mid_hits,eid_hits,space_hits) # some extra info
                
                if (success):
                    print("Success ", spid,nsession,eid, mid, lesson)
                    
                    if (lesson==mod_nlabs): # end for this module
                            mod_lab_done=True
                            break
                    else:
                        lesson+=1
                        if (labs_per_week ==1):
                            weekdone=True
                            nsession+=20 # skip 1 week
                        elif (labs_per_week ==2):
                            if (fails == 0):
                                nsession+=4 # skip 1 day
                            else:
                                nsession+=1 # skip 1 day
                else:
                    print("Trying Lab", fails, spid,nsession,eid, mid, lesson)
                    if (fails > 100):
                        print("Failed ", fails, spid,nsession,eid, mid, lesson)
                        #last_mod_first_session+=1
                        mod_lab_done=True
                        break
                    else:
                        nsession+=1 # try next session

                if nsession > 300:
                   #nsession=280
                   pass
                
                time.sleep(delay/5)     
        # week
    # module
    # not all sessions fall with in 300
                
def get_free_sessions(cursor, gid,semid):
    #return un allocated sessions
    
    free_sessions=[]
    sql='''SELECT * FROM semaster_calander AS SC INNER JOIN spaces ON SC.spid=spaces.spid
        WHERE SC.gid={} and SC.semid={} and SC.status=1 and nsession <= 300 order by nsession;
        '''
    #print(sql)
    sql=sql.format(gid,semid)
    
    cursor.execute(sql)
    cal_items = cursor.fetchall()
    free_sessions=[i+1 for i in range(300)]
    
    for i in range(len(cal_items)):
        ns=cal_items[i][4]
        if ns in free_sessions:
            free_sessions.remove(ns)

    return free_sessions

def last_good_session(cursor,gid, semid, sptype,this_mid, this_eid, this_session, this_nlesson):
    #what is the last lesson's nsession before this
    sql='''SELECT * FROM semaster_calander AS SC INNER JOIN spaces ON SC.spid=spaces.spid
        WHERE SC.gid={} and SC.semid={}  and SC.mid={} and SC.eid={} and SC.nlesson < {} and SC.status=1  and spaces.sptype={}  order by nsession desc;
        '''
    sql=sql.format(gid,semid, this_mid, this_eid, this_nlesson, sptype)
    #print(sql)
  
    cursor.execute(sql)
    prev_items = cursor.fetchall()
    if not (prev_items==[]):
        last_session=prev_items[0][4]
    else:
        last_session=0
    return last_session

    
def fix_semaster_calendar(cursor,gid, semid, sptype):
    sql='''SELECT * FROM semaster_calander AS SC INNER JOIN spaces ON SC.spid=spaces.spid
        WHERE SC.gid=1 and SC.semid=1 and SC.nsession > 300 and SC.status=1  and spaces.sptype={}  order by nsession;
        '''
    sql=sql.format(sptype)
    #print (sql)
    cursor.execute(sql)
    over300_calitems = cursor.fetchall()
    print("sessions to fix", len(over300_calitems))

    if not over300_calitems==[]:
        print ("Some Sessions over 300. Fixing ....")
        
        free_sessions=get_free_sessions(cursor,gid, semid)
        #print(free_sessions)
        if (free_sessions==[]):
            return free_sessions
        
        done_sessions=[]
        
        num_over300=len(over300_calitems)

        for n in range(num_over300):

            updating_spclid=over300_calitems[n][0]
            this_session= over300_calitems[n][4]
            this_eid=over300_calitems[n][6]
            this_mid=over300_calitems[n][7]
            this_nlesson=over300_calitems[n][8]
            this_spid=over300_calitems[n][3]
            this_sptype=over300_calitems[n][16]
            status=1
            
            
            # now we need last good session below this_lesson
            print("Trying to fix ", this_session, " at " , updating_spclid)
            last_nlesson=last_good_session(cursor,gid, semid, sptype,this_mid, this_eid, this_session, this_nlesson)

            if (last_nlesson == 0 or  last_nlesson >= 300): # no use skip
                print ("Skipping " , updating_spclid,this_session)
                continue # try next

            print("Last and Free Sessions ", last_nlesson, free_sessions)
            available_session=0

            for free in free_sessions:
                if free > last_nlesson:
                    available_session=free            
                    break
                
            if available_session==0:
                continue
            
            if available_session > 0:
                nday,nweek,nweekday,sesid=convert_session(available_session)
                sql='UPDATE semaster_calander SET nsession={}, nday={}, nweek={}, nweekday={}, sesid={} WHERE spclid={}'
                sql=sql.format(available_session,nday,nweek,nweekday,sesid,updating_spclid)
                print(sql)
                cursor.execute(sql)
                print ("Updated" , updating_spclid, this_session,available_session)
                free_sessions.remove(available_session)
                done_sessions.append((updating_spclid,this_session, available_session))
            
            #xdb.commit(conn)
            
        return done_sessions

def reorder_semaster_calendar(cursor,delay, gid, semid):
    
    sql='SELECT spclid FROM semaster_calander order by nsession;'
    cursor.execute(sql)
    cal_items = cursor.fetchall()
    new_session=1
    for item in cal_items:
        updating_spclid=item[0]
        nday,nweek,nweekday,sesid=convert_session(new_session)
        #print(new_session, nday,nweek,nweekday,sesid)
        sql='UPDATE semaster_calander SET nsession={}, nday={}, nweek={}, nweekday={}, sesid={} WHERE spclid={}'
        sql=sql.format(new_session,nday,nweek,nweekday,sesid,updating_spclid)
        cursor.execute(sql)
        print(new_session, " done")
        new_session+=1
        time.sleep(delay/5)
        
            
if __name__ == "__main__":
    
    delay=0.05
    conn=xdb.opendb('genetic56.db')
    cursor =conn.cursor() # create a cursor object
    
    success=crt_semaster_calander_table(cursor)
    # create cal for gid=1 and semid=1
    create_semaster_calander(cursor,delay,1,1) # generate modules
    xdb.commit(conn)
    
    #disp_semaster_calander(cursor)
    f=get_free_sessions(cursor, 1,1)
    print("Free Sessions")

    for e in f:
        print(e)
   
    done=fix_semaster_calendar(cursor, 1,1,1)
    xdb.commit(conn)

    print("Fixed Lectures ", done)

    done=fix_semaster_calendar(cursor, 1,1,2)
    xdb.commit(conn)
    
    print("Fixed Lab Works", done)

    
    print("Re-ordering Calender")
        
    reorder_semaster_calendar(cursor,delay,1, 1)
    xdb.commit(conn)

    success=crt_view_semaster_calender(cursor)
    xdb.commit(conn)
    
    xdb.closedb(conn)

