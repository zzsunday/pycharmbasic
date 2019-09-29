
#print(__import__('plugtest1'))
import importlib
def plugin_load(plugin_name:str, sep=':'):
    m,_,c = plugin_name.partition(sep)
    mod = importlib.import_module('m')
    getattr(mod, 'c')().showme()
    return cls()

if __name__ == '__main__' :
    #在需要的时候动态加载

    plugin_load('plugtest1:A').showme()