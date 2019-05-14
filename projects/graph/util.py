class Queue():
    def __init__(self, start=None):
        if start is None:
            self.queue = []
        else:
            self.queue = [start]
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self, start=None):
        if start is None:
            self.stack = []
        else:
            self.stack = [start]
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
