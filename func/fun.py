import inspect
def add(x:int,y:int,*args,**kwargs) ->int:
    return x+y

print(add.__annotations__)
sig=inspect.signature(add)
print(1,sig)
print(2,'params:',sig.parameters)
print(3,'return :',sig.return_annotation)
print(4, sig.parameters['y'])
print(5,sig.parameters['x'].annotation)
print(6,sig.parameters['args'])



