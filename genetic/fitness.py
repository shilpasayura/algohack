#fitness
import xdb

def crt_fitness_table(cursor):
    sql='''CREATE TABLE fitness (
	fitid INTEGER PRIMARY KEY AUTOINCREMENT,
	eid INTEGER,
        mid INTEGER,
	spid INTEGER,
	sessid INTEGER);
        '''
    success, count=xdb.runSQL(cursor, sql)
    return success
    
def insert_fitness(cursor,n,delay):   
    sql="SELECT * FROM fitness LIMIT 1";
    success, count=xdb.runSQL(cursor, sql)
    
    if (count > 0):
        print("fitness table: Records exist")
        return False, 0

    success, count=False,0 #reset

    #15 credits per semester, totals 120 credits after four years
    #7 * 1c + 4 * 2c =15 >----- < 4 x 5 * 15 = 300 sessions = 20 * 7 + 40 * 4  
    # 2 * 11 * 10 + 4 * 4 * 5=300  lectures and lab distributed to get 299 sessions
    sqls=""
   #data : weeks, lectures, labworks for 11 fitness=n (299)
    n=11 # safety
    mwll_arr=[(10,1,1),(10,1,1),(10,1,1),(10,1,1),(10,1,1),(10,1,1),(10,1,1),(14,1,1), (15,1,1), (15,2,1), (14,2,2)]
    
    #for a in mod_weekly_freq_nweeks:
    #	sum=sum+ a[0] * (a[1]+a[2])
	
    for i in range (n):
        name="Module " + str(i+1)
        
        #print(i,n,name)
        nweeks,nlect,nlab=mwll_arr[i]
        
        step=1  # 1- every day, every 2nd day, every week  
        sql='INSERT INTO fitness (name,weeks, lectures, labworks) VALUES ('+ '"{}" , {}, {}, {}'.format(name, nweeks,nlect,nlab) +');'
        #print (sql)
        sqls=sqls + sql
        
    success , count=xdb.runSQL_stmts(cursor, sqls,delay)
    return success, count

if __name__ == "__main__":
    conn=xdb.opendb('genetic4.db')
    cursor =conn.cursor() # create a cursor object
    print(crt_fitness_table(cursor))


