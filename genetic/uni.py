#uni.py
'''
AlgoHack Genetic Algorithm for University Semaster Planning
Version 0.03 2018
Niranjan Meegammana Shilpasayura.org
'''

import xdb
import educator
import modules
import educator_modules
import spaces
import sessions
import semaster_calander

delay=0.05 # 50 ms
#open gentic database
conn=xdb.opendb('genetic44.db')
cursor =conn.cursor() # create a cursor object
# gid : groupid 1
# semid, semasterid 1

success=modules.crt_modules_table(cursor) # create modules table
success, count =modules.insert_modules(cursor,11,delay,1,1) # generate modules
xdb.commit(conn)
print ('modules Done--------------------')
   
success=educator.crt_educators_table(cursor,True) # create lecturers table
success, count =educator.insert_educators(cursor,11,delay) # generate  lecturers
xdb.commit(conn)
print ('Educator Done--------------------')

success=spaces.crt_spaces_table(cursor) # create spaces table
#cursor, nlect,nlabs,gid,semid, delay
success, count =spaces.insert_spaces(cursor,1,1,1,1,delay) # generate spaces
print ('Spaces Done --------------------')

success=sessions.crt_sessions_table(cursor) # create sessions table
success, count =sessions.insert_sessions(cursor,1,delay) # generate sessions
print ('Sessions Done --------------------')

print ('Educator Modules --------------------')

success=educator_modules.crt_educator_modules_table(cursor, True) # create modules table
success, count =educator_modules.insert_educator_modules(cursor,11,delay,1,1) # generate modules
xdb.commit(conn)

educator_modules.disp_educator_modules(cursor,"educator_modules") # display edu mods

print ('Improving Educator Modules --------------------')

success=educator_modules.crt_improved_educator_modules_table(cursor, True) # create imp lect mods table
success=educator_modules.balance_educator_modules(cursor,1,1) # balance edu mods
xdb.commit(conn)

print ('Improved Educator Modules List --------------------')
educator_modules.disp_educator_modules(cursor,"improved_educator_modules") # list new edu mods

success=educator_modules.crt_view_improved_eductor_modules(cursor) # create view
xdb.commit(conn)
print ('Improved View Done--------------------')


success=semaster_calander.crt_semaster_calander_table(cursor)

# create cal for gid=1 and semid=1
success=semaster_calander.create_semaster_calander(cursor,1,delay,1,1) # generate modules
xdb.commit(conn)
print ('Semaster Calender Created --------------------')
success=semaster_calander.crt_view_semaster_calender(cursor)
print ('Semaster Calender View Done--------------------')
semaster_calander.disp_semaster_calander(cursor)
print ('Done! thank you for waiting')
xdb.commit(conn)
if (conn !=None):
    xdb.closedb(conn)
