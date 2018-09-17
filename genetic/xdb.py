#xdb.py
'''
AlgoHack Genetic Algorithm for University Semaster Planning
Version 0.03 2018
Niranjan Meegammana Shilpasayura.org
'''
import sqlite3 
import time

def commit(conn):
    conn.commit()
    
def opendb(db):
    try:
        conn= sqlite3.connect(db)
        print (conn) 
        print ('db connection established')
    except (sqlite3.Error,) as e:
        conn=None
        print(e)
    finally:
        return conn
        
def closedb(conn):
    conn.close()
    print ('db connection closed')

def runSQL(cursor, sql):
    success=False
    count=0
    
    try:
        cursor.execute(sql)
        count=len(cursor.fetchall()) # get count of rows affected
        success=True
        print (sql, ":", count, ' done')
    except (sqlite3.Error,) as e:
        print(e)
    finally:
        return success, count

def runSQL_stmts(cursor,sql_stmts,delay):

    success, count = False, 0
    
    sql_array=sql_stmts.split(";")
       
    for sql in sql_array:
        
        try:
            cursor.execute(sql)
            count=count+1
            success=True
            print (sql, ":", count, ' done')
        except (sqlite3.Error,) as e:
            print(e)
        finally:
            pass
            time.sleep(delay)

    return success, count
    
   
if __name__ == "__main__":
    conn=opendb()
    if (conn !=None):
        closedb(conn)

    
