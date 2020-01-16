class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pushAtStart(self,item):
        self.items.insert(0,item)

    def pop(self):
        self.items.pop()

    def popAtEnd(self):
        self.items.pop(0)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)