class Add:
    def __init__(self):
        self.x = x

    def __add__(self, other):
        print('add', self)
        return self.x + other.x

    def __iadd__(self, other):
        print('iadd', self)
        return self.x + other.x

    def __radd__(self, other):
        print('radd', self)