import threading
import time
class MyThread(threading.Thread):

    def start(self) -> None:
        print('start')
        super().start()

    def run(self) -> None:
        print('run')
        super().run()
def worker():
    print(threading.current_thread())
    for _ in range(5):
        time.sleep(0.5)
        print('1.............')
    print('1==================')

def worker1():
    print(threading.current_thread())
    for _ in range(5):
        time.sleep(0.5)
        print('2.............')
    print('2==================')

t = MyThread(target=worker,name = 'w1')
t.start()
#t.run()
t1 = MyThread(target=worker1,name = 'w1')
#t1.run()
t1.start()