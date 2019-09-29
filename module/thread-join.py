import threading
import logging
logging.basicConfig(level=logging.INFO)

def worker():
    for x in range(50):
        msg= '{} is running'.format(threading.current_thread())
        logging.info(msg)
        t = threading.Thread(target=worker, name='work = 0', daemon=True)
        #t.start()
        #t.join()
def worker1():
    for x in range(50):
        msg= '$$$$${} is running'.format(threading.current_thread())
        logging.info(msg)

t = threading.Thread(target=worker, name='work = 0', daemon=True)
t.start()
#t.join() #谁调用谁等待

print('ending')
print('outer',threading.enumerate())