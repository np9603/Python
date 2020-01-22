from LinkedList import LinkedNode

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self,data):
        temp = LinkedNode.Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self,data):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is data:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,data):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() is data:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
