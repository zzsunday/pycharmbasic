class Temperature:
    def __init__(self,t,unit='c'):
        self._c = None  #不加下划线为什么不能调用
        self._f = None
        self._k = None
        if unit=='k':
            self._k=t
            self._c=self.k2c(t)
        elif unit =='f':
            self._f=t
            self. _c=self.f2c(t)
        else:
            self._c=t

    @property
    def c(self):
        return self._c
    @property
    def k(self):
        if self._k is None: #考虑为什么不用==
            self._k=self.k2c(self._c)
        return self._k
    @property
    def f(self):
        if self._f is None:
            self._f=self.f2c(self._c)
        return self._f

    @classmethod
    def c2f(cls,c):
        return 9*c/5+32
    @classmethod
    def c2k(cls,c):
        return c+273.15
    @classmethod
    def f2c(cls,c):
        return 5*(c-32)/9
    @classmethod
    def f2k(cls,c):
        return cls.c2k(cls.f2c())
    @classmethod
    def k2c(cls,c):
        return c-273.15
a=Temperature(39)
print(a.k)
