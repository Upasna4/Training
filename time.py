import time

secs = time.time()      #from 1 Jan 1970
print(secs)

c=time.clock()
print(c)

lt=time.localtime(time.time())
print(lt)

asc=time.asctime(time.localtime(time.time()))
print(asc)

u="upasna"
for i in range(0,5):
    time.sleep(1)
    print(u)
