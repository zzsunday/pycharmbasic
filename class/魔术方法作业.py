class SingeNode:
    def __init__(self, val, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.val  = val

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.items = []  # 不需要插入的列表，检索方便，但是插入的话就不合适
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val):
        node = SingeNode(val)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.items.append(node)

    def insert(self, index, val):
        if index < 0:
            raise Exception('Error')
        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is None:
            self.append(val)
            return

        prev = current.prev

        node = SingeNode(val)
        if prev is None:  # 开头
            self.head = node
            node.next = current
            current.prev = node
        else:
            node.prev = prev
            node.next = current
            current.prev = node
            prev.next = node
        self.items.insert(index, node)

    def pop(self):
        if self.tail is None:
            raise Exception('Empty')
        tail = self.tail
        prev = tail.prev
        # next = tail.next #None
        if prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = prev
            prev.next = None
        self.items.pop()
        return tail.val

    def remove(self, index):
        if self.tail is None:
            raise Exception('Empty')

        if index < 0:  # 不接受负数
            raise IndexError('Not negative index{}'.format(index))

        current = None
        for i, nodex in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        else:  # Not found
            raise IndexError('wrong index {}'.format(index))

        prev = current.prev
        next = current.next

        # 4种情况
        if prev is None and next is None:  # only one node
            self.head = None
            self.tail = None
        elif prev is None:  # 头部
            self.head = next
            next.prev = None
        elif next is None:  # 尾部
            self.tail = prev
            self.next = None
        else:  # 在中间
            prev.next = next
            next.prev = prev

        del current
        self.items.pop(index)

    def iternodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.prev if reverse else current.next

    def getitem(self, index):
        if index < 0:
            return None
        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is not None:
            return current

    def __getitem__(self, item):
        return self.nodes(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        node = self[index]
        node.val = value #node
        return self.items

    def __iter__(self):
        return self.iternodes()