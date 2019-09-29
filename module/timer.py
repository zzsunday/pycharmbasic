import threading
import time
def add(x,y):
    print(x+y)

t = threading.Timer(15,add,args=(4,5))
#t.cancel()
t.start()
time.sleep(1)
t.cancel()
