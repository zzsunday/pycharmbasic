import functools
import time

@functools.lru_cache()
def add(x,y=5):
    time.sleep(3)
    ret = x+y
    print(ret)
    return ret

add(4)