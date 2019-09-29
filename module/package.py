# import m.x
# from m.x.x1 import *
# import m.x as mx
# import pack
# import m.m1
from m import m1 #不会导入私有属性（非下划线开头）
print(dir())
# print(locals())
print(m1.m1)


# print(m.__file__)
# print(m.__cached__)
# print(m.y)
# print(type(pack))
# print(pack)
# print(pack.x)
# print(mx.xname)