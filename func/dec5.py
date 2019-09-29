# def copy_properties(src):
#     def _copy(dst):
#         dst.__name__ = src.__name__
#         dst.__doc__  = src. __doc__
#         return dst
#     return _copy()

def logger(fn):
    def wrapper(*args,**kwargs):
        '''I am a warrper'''
        print('begin')
        ret=fn(*args,**kwargs)
        print('end')
        return ret
    return wrapper

@logger
def add(x,y):
    '''This is a function for add'''
    return x+y
print('name={},doc={}'.format(add.__name__,add.__doc__))