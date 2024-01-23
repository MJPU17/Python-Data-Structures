from DequeList import DequeList

class QueueImp:

    def __init__(self):
        self.infos=DequeList()

    def enqueue(self, info):
        self.infos.insertLast(info)

    def dequeue(self):
        return self.infos.removeFirst()

    def size(self):
        return self.infos.size

    def isEmpty(self):
        return self.infos.isEmpty()

    def peek(self):
        return self.infos.head.info

    def __iter__(self):
        return self.infos.__iter__()

    def __next__(self):
        return self.infos.__next__()

    def clear(self):
        self.infos.clear()

