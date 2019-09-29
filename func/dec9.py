import functools
def logger(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        '''I am a warrper'''
        print('begin')
        ret = fn(*args,**kwargs)
        print('end')
        return ret
    # functools.update_wrapper(wrapper,fn)
    print('{},{}'.format(id(wrapper),id(fn)))
    return wrapper
@logger#add=logger(add)
def add(x,y):
    '''this is a function for add'''
    return x+y
print('name={},doc={}'.format(add.__name__,add.__doc__))
print(id(add.__wrapped__))
