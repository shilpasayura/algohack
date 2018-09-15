#spaces.py
'''
AlgoHack Genetic Algorithm for University Semaster Planning
Version 0.03 2018
Niranjan Meegammana Shilpasayura.org
'''

import xdb

def crt_spaces_table(cursor,drop=False):
    if (drop):
        sql="DROP TABLE IF EXISTS spaces;"
        success, count=xdb.runSQL(cursor, sql)

    sql='''CREATE TABLE IF NOT EXISTS spaces (
    spid INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(30),
    sptype INTEGER,
    fitness INTEGER,
    gid INTEGER DEFAULT 0,
    semid INTEGER DEFAULT 0)
    '''
    success, count=xdb.runSQL(cursor, sql)
    return success
    
def insert_spaces(cursor,nlect,nlabs,gid,semid, delay):
    # nlabs is number of labs
    # nlecs is number of lecture halls
    # if gid =0 common for all groups else dedicated
    # if semid=0 common for all semasters else dedicated
    sql="SELECT * FROM spaces LIMIT 1";
    success, count=xdb.runSQL(cursor, sql)
    
    if (count > 0):
        print("spaces table: Records exist")
        return False, 0

    sqls=""
    fitness=1
    for i in range (nlect):
        name="Lect Hall " + str(i+1)
        sptype=1
        sqls=sqls +'INSERT INTO spaces (name,sptype,fitness,gid,semid) VALUES ('+ '"{}",{}, {},{},{}'.format(name, sptype,fitness,gid,semid) +');'

    for i in range (nlabs):
        name="Lab " + str(i+1)
        sptype=2
        sqls=sqls +'INSERT INTO spaces (name,sptype,fitness,gid,semid) VALUES ('+ '"{}",{}, {},{},{}'.format(name, sptype,fitness,gid,semid) +');'

    success, count=xdb.runSQL_stmts(cursor, sqls,delay)
    return success, count
    
if __name__ == "__main__":
    delay=0.05
    conn=xdb.opendb('genetic44.db')
    cursor =conn.cursor() # create a cursor object
    success=crt_spaces_table(cursor, True) # create spaces table
    #dedicated lecture hall, lab for group and semaster
    success, count =insert_spaces(cursor,1,1,1,1,delay) # generate records
    xdb.commit(conn)
    xdb.closedb(conn)
