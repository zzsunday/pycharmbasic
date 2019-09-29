import functools
import time
import inspect
import datetime
def s_cache(t):
    def _cache(fn):
        local_cache={}
        @functools.wraps(fn)
        def wrapper(*args,**kwargs):
            #local_cache有没有过期的key
            expire_key=[]
            for k,(_,ts) in local_cache.items():
                if datetime.datetime.now().timestamp()-ts > t:
                    # local_cache.pop(k) 考虑这个为什么不行
                    expire_key.append(k)
            for k in expire_key:
                local_cache.pop(k) #后期可以考虑并行运算

            # print(args,kwargs)
            key_dict={}#sorted
            sig=inspect.signature(fn)
            dit= sig.parameters#ordereddict
            param_list=list(dit.keys())
            #位置参数
            for i,v in enumerate(args):
                # print(i,v)
                k=param_list[i]
                key_dict[k]=v
            key_dict.update(kwargs)
            for k in dit.keys():
                if k not in key_dict.keys():
                    key_dict[k]=dit[k].default
            key=tuple(key_dict.items())
            if key not in local_cache.keys():
                ret = fn(*args, **kwargs)
                local_cache[key]=(ret,datetime.datetime.now().timestamp())

            return local_cache[key]
        return wrapper
    return _cache
def logger(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        start=datetime.datetime.now()
        ret=fn(*args,**kwargs)
        delta=(datetime.datetime.now()-start).total_seconds()
        print(delta)
        return  ret
    return wrapper
@logger
@s_cache(3)
def add(x,y=5):
    time.sleep(3)
    ret = x+y
    return ret

add(4)
add(4,5)
add(x=4,y=5)
add(y=5,x=4)
