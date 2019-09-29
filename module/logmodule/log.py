import threading
import time
import logging
FORMAT = "%(asctime)s %(thread)d %(message)s %(school)s"
logging.basicConfig(level=logging.INFO,format=FORMAT,datefmt='%Y-%m-%D-%H:%M:%S',filename='test.log')
#filename='test.log' 加到上面中可以重定向
d = {'school':'corgi'}
def add(x,y):
    logging.info('{}{}'.format(threading.enumerate(),x+y),extra = d)
    #logging.warning("%s %s",x,y)
    #logging.debug("{}{}".format(str(x),str(y)))

t = threading.Timer(0.1,add,args=(4,5))
#t.cancel()
t.start()

log = logging.getLogger('a')
print(log.name)
print(type(log))