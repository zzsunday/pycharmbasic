import inspect
def add(x,y:int=7,*args,z,t=10,**kwargs)->int:
    return x+y

sig=inspect.signature(add)
print(sig)

print('params :', sig.parameters)
print('retunr :',sig.return_annotation)
print('=========================')


for i,(name,param) in enumerate(sig.parameters.items()):
    print(i+1,name,param.annotation,param.kind,param.default)
    print(param.default is param.empty,end='\n\n')