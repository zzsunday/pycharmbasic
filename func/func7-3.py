def cmds_dispatch:
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
    return reg,dispatch
reg,dispatch=cmds_dispatch() #本题精髓

@reg('corgi')
def foo1():
    print('welcome to the corgi da house')
@reg('py')
def foo2():
    print('python')

dispatch()
