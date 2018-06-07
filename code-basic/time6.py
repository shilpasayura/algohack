import time
def clock():
    ut=time.time()
    lt = time.localtime(ut)
    tm=str(lt.tm_hour) + ":" + str(lt.tm_min) + ":" + str(lt.tm_sec)
    print (tm)

clock()
