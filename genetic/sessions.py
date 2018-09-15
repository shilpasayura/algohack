#sessions.py

import xdb

def crt_sessions_table(cursor,drop=False):
    if (drop):
        sql="DROP TABLE IF EXISTS sessions;"
        success, count=xdb.runSQL(cursor, sql)
    
    sql='''CREATE TABLE IF NOT EXISTS sessions (
        sesid INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(30), tfr INTEGER, tto INTEGER, fitness )
        '''
    success, count=xdb.runSQL(cursor, sql)
    return success
    
def insert_sessions(cursor,n,delay):   
    sql="SELECT * FROM sessions LIMIT 1";
    success, count=xdb.runSQL(cursor, sql)
    
    if (count > 0):
        print("sessions table: Records exist")
        return False, 0

    sqls=""
    session_name_arr=["Morning 1", "Morning 2", "Afternoon 1", "Afternoon 2"]
    session_data=[(8,10,4),(10,12,3),(13,15,2),(15,17,1)]
    
    i=0
    for i in range(4):
        name=session_name_arr[i]
        tfr,tto,fitness=session_data[i]
      
        sql='INSERT INTO sessions (name,tfr,tto,fitness) VALUES ('+ '"{}" , {}, {}, {}'.format(name, tfr, tto,fitness) +");"
        print(sql)
        sqls=sqls+sql

    success, count=xdb.runSQL_stmts(cursor, sqls,delay)

    return success, count
    

if __name__ == "__main__":
    delay=0.05
    conn=xdb.opendb('genetics2111.db')
    cursor =conn.cursor() # create a cursor object
    success=crt_sessions_table(cursor, True) # create spaces table
    success, count =insert_sessions(cursor,1,delay) # generate modules
    xdb.commit(conn)
    xdb.closedb(conn)
