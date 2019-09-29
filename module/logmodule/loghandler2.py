import threading
import time
import logging
FORMAT = "%(asctime)s %(thread)d %(message)s "
logging.basicConfig(level=logging.ERROR,format=FORMAT,datefmt='%Y-%m-%D-%H:%M:%S' )


root = logging.getLogger()
print(root,id(root))

log1 = logging.getLogger('s')
log1.setLevel(logging.INFO)
print(log1.getEffectiveLevel())


#handlr = logging.StreamHandler()
handlr =logging.FileHandler('handler.log') #并没有输出到文件中
handlr.setLevel(logging.INFO)
log1.addHandler(handlr)

#log1.info('log1 info')

log2 = logging.getLogger('s.s1')
#log2.setLevel(20)
print('log2 level:',log2.getEffectiveLevel())
handlr2 =logging.FileHandler('handler2.log')
handlr2.setLevel(logging.INFO)
log2.addHandler(handlr2)

log2.info('log2 info')