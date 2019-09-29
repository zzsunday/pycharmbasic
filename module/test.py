
print('test module')
import test1

if __name__ == "__main__":
    print('in main')
else:
    print('in module {}'.format(__name__))
print(__file__)
print(__package__)
# b = test1.A()
# print(dir())
# b.show()
# print(__name__)

# import test2
#
# print('local module')
#
# import test2