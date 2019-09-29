import threading
import time

# class A:
#     def __init__(self,x):
#         self.x = x
a = threading.local()

def worker():
    a.x = 0
    for i in range(10):
        time.sleep(0.0001)
        a.x +=1
        print(a.__dict__)
    print(threading.current_thread(),a.x)

for i in range(5):
    threading.Thread(target=worker).start()