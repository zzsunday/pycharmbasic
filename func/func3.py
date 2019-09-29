def check(fn):
    def wrapper(*args,**kwargs):
    #实参检查
        print(args,kwargs)
        sig=inspect.signature(fn)
        params = sig.parameters#只读的有序字典
        print(params)
        # for param in sig.parameters.values():
        #     print(param.name,param)
        #     print(param.name,param.annotation,param.kind,param.default)
        # ret = fn (*args,**kwargs)
        params_list=list(params.keys())
        for i,v in enumerate(args):
            k=params_list[i]
            if isinstance(v, params[k].annotation):
                print(v, 'is', params[k].annotation)
            else:
                print(v, 'is not', params[k].annotation)


        for k,v in kwargs.items():#关键字参数
            if isinstance(v,params[k].annotation):
                print(v,'is',params[k].annotation)
            else:
                print(v,'is not',params[k].annotation)
        ret=fn(*args,**kwargs)
        return ret
    return wrapper

