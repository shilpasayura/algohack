#modules
import xdb
import data

def crt_modules_table(cursor,drop=False):
    if (drop):
        sql="DROP TABLE IF EXISTS modules;"
        success, count=xdb.runSQL(cursor, sql)
    
    sql='''CREATE TABLE modules (
	mid INTEGER PRIMARY KEY AUTOINCREMENT,
	name varchar(30),
        weeks INTEGER DEFAULT 0,
	lectures INTEGER DEFAULT 0,
	labworks INTEGER DEFAULT 0,
	fitness INTEGER DEFAULT 0,
	leclab_gap INTEGER DEFAULT 1,
	gid INTEGER DEFAULT 0,
	semid INTEGER DEFAULT 0)
        '''
    success, count=xdb.runSQL(cursor, sql)
    return success
    
def insert_modules(cursor,n,delay,gid,semid):   
    sql="SELECT * FROM modules LIMIT 1";
    success, count=xdb.runSQL(cursor, sql)
    
    if (count > 0):
        print("modules table: Records exist")
        return False, 0

    success, count=False,0 #reset

    #15 credits per semester, totals 120 credits after four years
    #7 * 1c + 4 * 2c =15 >----- < 4 x 5 * 15 = 300 sessions = 20 * 7 + 40 * 4  
    # 2 * 11 * 10 + 4 * 4 * 5=300  lectures and lab distributed to get 299 sessions
    sqls=""
   #data : fitness, weeks, lectures, labworks for 11 modules=n (299)
    n=11 # safety
    mwll_arr=data.module_data() # read data
    #for a in mod_weekly_freq_nweeks:
    #	sum=sum+ a[0] * (a[1]+a[2])
	
    for i in range (n):
        name="Module " + str(i+1)
        
        #print(i,n,name)
        fitness,nweeks,nlect,nlab=mwll_arr[i]
        
        step=1  # 1- every day, every 2nd day, every week
        leclab_gap=1 # days : lecture and lab sessions minumm gap  
        sql='INSERT INTO modules (name,weeks, lectures,labworks,fitness,leclab_gap,gid,semid) VALUES ('+ '"{}" , {}, {}, {}, {},{},{}, {}'.format(name, nweeks,nlect,nlab,fitness,leclab_gap,gid,semid) +');'
        #print (sql)
        sqls=sqls + sql

    success , count=xdb.runSQL_stmts(cursor, sqls,delay)
    return success, count

if __name__ == "__main__":

    delay=0.05
    conn=xdb.opendb('genetic56.db')
    cursor =conn.cursor() # create a cursor object
    success=crt_modules_table(cursor,True) # create spaces table
    success, count =insert_modules(cursor,11,delay,1,1) # generate modules
    xdb.commit(conn)
    xdb.closedb(conn)

