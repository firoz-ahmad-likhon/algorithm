class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        return self.stack

    def pop(self):
        self.stack.pop()
        return self.stack


cls = Stack()
print(cls.stack)
print(cls.push(1))
print(cls.push(2))
print(cls.push(3))
print(cls.pop())
print(cls.pop())
print(cls.pop())
