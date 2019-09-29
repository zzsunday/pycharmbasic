import threading
import logging
logging.basicConfig(level=logging.INFO)

def worker():
    for x in range(50):
        msg= '{} is running'.format(threading.current_thread())
        logging.info(msg)
        print(threading.enumerate())

def worker1():
    for x in range(50):
        msg= '$$$$${} is running'.format(threading.current_thread())
        logging.info(msg)




threading.Thread(target=worker, name='work = 0', daemon=True).start()
threading.Thread(target=worker1, name='work = 0').start()
print('ending')
print('outer',threading.enumerate())