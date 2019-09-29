
command={}
def reg(name):
    def _reg(fn):
        command[name]=fn
        return fn
    return _reg
def defaultfunc():
    print('Unknown command')

def dispatch():
    while True:
        cmd=input('>>')
        if cmd.strip()== 'quit':
            return
        command.get(cmd,defaultfunc)()

@reg('corgi')
def foo1():
    print('welcome to the corgi da house')
@reg('py')
def foo2():
    print('python')

if __name__== '__main__ ':
    dispatch()

dispatch()

