import threading
import time


def worker1():
    print('inside1',threading.current_thread())
    print('inside2',threading.main_thread())
    print('inside3',threading.active_count())
    print('inside4',threading.enumerate())
    print('inside5',threading.main_thread().is_alive())
    for _ in range(5):
        time.sleep(0.5)
        print('1....................')
    print('1==================')

print('outer',threading.current_thread())
t = threading.Thread(target=worker1)
t.start()
print(threading.enumerate())
print(threading.main_thread().is_alive())
