#eductor
'''
AlgoHack Genetic Algorithm for University Semaster Planning
Version 0.03 2018
Niranjan Meegammana Shilpasayura.org
'''

import xdb



def crt_educators_table(cursor,drop=False):
    if (drop):
        sql="DROP TABLE IF EXISTS educators;"
        success, count=xdb.runSQL(cursor, sql)
    
    sql='''CREATE TABLE IF NOT EXISTS educators (
        eid INTEGER PRIMARY KEY AUTOINCREMENT,
        name varchar(30),
        fitness INTEGER,
        step INTEGER,
        gid INTEGER DEFAULT 0,
        semid INTEGER DEFAULT 0)
        '''
    success, count=xdb.runSQL(cursor, sql)
    return success
    
def insert_educators(cursor,n,delay):
    
    sql="SELECT * FROM educators LIMIT 1";
    success, count=xdb.runSQL(cursor, sql)
    
    if (count > 0):
        print("educators table: Records exist")
        return False, 0

    sqls=""
    
    for i in range (n):
        name="Lecturer " + str(i+1)
        fitness=1
        step=1  # 1- every day, every 2nd day, every week
        #here we assume every educator is teaching all semasters and groups
        #else algorithm or data set need to give semid and gid
        semid=0 # 0 : all or 1-8: semaster number 
        gid=0   # 0 : all or 1-4: group no
        sqls=sqls + 'INSERT INTO educators (name,fitness, step,gid,semid) VALUES ('+ '"{}" , {}, {},{},{}'.format(name, fitness, step,gid,semid) +');'
            
    success, count=xdb.runSQL_stmts(cursor, sqls,delay)
    return success, count

if __name__ == "__main__":
    
    delay=0.05
    conn=xdb.opendb('genetic4461.db')
    cursor =conn.cursor() # create a cursor object
    success=crt_educators_table(cursor,True) # create spaces table
    success, count =insert_educators(cursor,11,delay) # generate modules
    xdb.commit(conn)
    xdb.closedb(conn)
    


