class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return self.queue

    def dequeue(self):
        self.queue.pop(0)
        return self.queue

cls = Queue()
print(cls.queue)
print(cls.enqueue(1))
print(cls.enqueue(2))
print(cls.enqueue(3))
print(cls.dequeue())
print(cls.dequeue())
print(cls.dequeue())
