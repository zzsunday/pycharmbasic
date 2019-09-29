import threading
import time
import logging
FORMAT = "%(asctime)s %(thread)d %(message)s "
logging.basicConfig(level=logging.INFO,format=FORMAT,datefmt='%Y-%m-%D-%H:%M:%S' )
#filename='test.log' 加到上面中可以重定向
d = {'school':'corgi'}
# def add(x,y):
#     log = logging.getLogger('a')
#     print('---',log.name)
#     print('===',type(log),log.parent)
#     log.info('{}{}'.format(threading.enumerate(),x+y),extra = d)
#     log.debug('{}{}'.format(threading.enumerate(), x + y), extra=d)
    #logging.warning("%s %s",x,y)
    #logging.debug("{}{}".format(str(x),str(y)))

#t = threading.Timer(0.1,add,args=(4,5))
#t.cancel()
#t.start()

root = logging.getLogger()
root.info('my root')
print(root,id(root))
print('==============')
loga = logging.getLogger('a')
print(loga,id(loga),id(loga.parent))
root.info('my a')
print('===========')
loga = logging.getLogger('a.b')
print(loga,id(loga),id(loga.parent))
root.info('my a.b')