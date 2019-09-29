import threading
import time
import logging
FORMAT = "%(asctime)s %(thread)d %(message)s "
logging.basicConfig(level=logging.ERROR,format=FORMAT,datefmt='%Y-%m-%D-%H:%M:%S' )


root = logging.getLogger()
print(root,id(root))

log1 = logging.getLogger('s') #只要是传入的名字一样，实例就只有一个
log1.setLevel(logging.WARNING)
print(log1.getEffectiveLevel())


handlr = logging.StreamHandler()
handlr =logging.FileHandler('handler.log') #并没有输出到文件中
handlr.setLevel(logging.INFO)
fmt1 =logging.Formatter('%(asctime)s %(thread)d %(message)s')
handlr.setFormatter(fmt1)
log1.addHandler(handlr)



#log1.info('log1 info')

log2 = logging.getLogger('s.s1')
log2.setLevel(20)
print('log2 level:',log2.getEffectiveLevel())
handlr2 =logging.FileHandler('handler2.log')
handlr2.setLevel(logging.INFO)
fltr = logging.Filter('s.s2') #改成s.s1呢
handlr2.addFilter(fltr)
log2.addHandler(handlr2)

log2.info('log2 info')