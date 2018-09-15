#db.py

import sqlite3 

def opendb():
    try:
        conn= sqlite3.connect('genetic.db')
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
    
if __name__ == "__main__":
    conn=opendb()
    if (conn !=None):
        closedb(conn)

    
