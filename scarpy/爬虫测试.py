class RandomGenerator:
    def __init__(self,start=0,stop=100,count=10):
        self.start=start
        self.stop=stop
        self.count=count
        self.gen=self._generator()
    def _generator(self):
        while True:
            yield random.randint(self.start,self.stop)
    def generator(self):
            return [next(self.gen) for _ in