import threading
import time
import logging
FORMAT = "%(asctime)s %(thread)d %(message)s "
logging.basicConfig(level=logging.WARNING,format=FORMAT,datefmt='%Y-%m-%D-%H:%M:%S' )

root = logging.getLogger()
root.info('my root')

loga = logging.getLogger(__name__)
loga.setLevel(logging.WARNING) #改成error呢
print(loga.getEffectiveLevel())

logachid = logging.getLogger(__name__+'.child')  #继承到loga
logachid.warning('log2 warning')