# from collections import deque
from queue import Queue
def hotPotato(input,num):

    # queue = deque()
    queue = Queue()
    for name in input:
        queue.put(name)

    while queue.qsize() > 1:
        for i in range(num):
            queue.put(queue.get())

        queue.get()

    return queue.get()

def main():
    names = ["Brad","Kent","Jane","Susan","David","Bill"]

    print(hotPotato(names,7))

    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


main()