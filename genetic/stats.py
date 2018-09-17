#stats.py
import xdb

def count_recs(cursor,gid,semid,exsql):
    sql='select count(*) from semaster_calander where gid={} and semid={} {};'
    sql=sql.format(gid,semid, exsql)
    cursor.execute(sql)
    count = cursor.fetchone()[0]
    return count

def semaster_stats(cursor,gid,semid):
    
    print("Semaster Statistics")
    n1=count_recs(cursor,gid,semid,"and sptype=1 and sesid < 3")
    print("Lectures in Morning : " , n1)
    
    n2=count_recs(cursor,gid,semid,"and sptype=1 and sesid > 2")
    print("Lectures in Afternoon : " , n2)  
    
    n3=count_recs(cursor,gid,semid,"and sptype=2 and sesid < 3")
    print("Lab Sessions in Morning  : " , n3)  
    
    n4=count_recs(cursor,gid,semid,"and sptype=2 and sesid > 2")
    print("Lab Sessions in Afternoon  : " , n4)  

    print("Total Sessions  : " , (n1+n2+n3+n4))
    
    sql='''SELECT distinct SC.mid, modules.name FROM semaster_calander AS SC
    INNER JOIN modules, spaces ON SC.mid=modules.mid and SC.spid=spaces.spid where SC.gid={} and SC.semid={} order by SC.mid;
    '''
    sql=sql.format(gid,semid)
    cursor.execute(sql)
    module_stats={}
    modules = cursor.fetchall()
    print("")
    print("Module : [Lect Mo:Lect Af]", "[Lab Mo: Lab Af]")
    
    for m in modules:
        mid=m[0]
        mname=m[1]
       
        
        exsql_lect_mor="and mid=" + str(mid) + " and sptype=1 and sesid < 3"
        lect_mn=count_recs(cursor,gid,semid,exsql_lect_mor)
        
        exsql_lect_aft="and mid=" + str(mid) + " and sptype=1 and sesid > 2"
        lect_af=count_recs(cursor,gid,semid, exsql_lect_aft)

        exsql_lab_mor="and mid=" + str(mid) + " and sptype=2 and sesid < 3"
        lab_mn=count_recs(cursor,gid,semid,exsql_lab_mor)
        
        exsql_lab_aft="and mid=" + str(mid) + " and sptype=2 and sesid > 2"
        lab_af=count_recs(cursor,gid,semid,exsql_lab_aft)
        s1="[" + str(lect_mn) +" : " + str(lect_af) + "]"
        s2="[" + str(lab_mn) +" : " + str(lab_af) + "]"
        print(mname, ":", s1, s2)
        
        

if __name__ == "__main__":
    delay=0.05
    conn=xdb.opendb('genetic56.db')
    cursor =conn.cursor() # create a cursor object
    semaster_stats(cursor,1,1)
    xdb.closedb(conn)
