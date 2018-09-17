import sqlite3 

try:
    conn= sqlite3.connect('test.db')
    print (conn) 
    print ('connection established')
    cursor =conn.cursor() # create a cursor object

    sql1="""
    CREATE TABLE users (
    uid INTEGER PRIMARY KEY AUTOINCREMENT 
    NOT NULL, name text);
    """

    print ("Table created")
           
    sql2="INSERT INTO users (name) VALUES('Ama');"       
    sql3="INSERT INTO users (name) VALUES('Bima');"
    cursor.execute(sql2)
    cursor.execute(sql3)
    conn.commit()
    sql4="SELECT * FROM users;"
    cursor.execute(sql4)

    for row in cursor.fetchall(): 
        # row is a tuple
        #print(row, row[2])
        uid, name = row
        print(uid, name)

    cursor.execute(sql1)
    
    conn.close()
except (sqlite3.Error,) as e:
    print(e)
finally:
    print("end")


    

    


    
