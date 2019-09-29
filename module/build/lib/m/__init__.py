print(__name__)
mpro = 123

_x = 'm,_x'

__y = 'm,__y'
# print('m module=',dir())
# print('m module=',locals().keys())

__all__ = ['_x', 'm1']
from . import m1


# def foo():
#     x = 5
#     print('m module=', locals().keys())
#     print('m module=', dir())