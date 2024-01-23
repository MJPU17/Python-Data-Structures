from DequeList import DequeList

class StackImp:

    def __init__(self):
        self.infos=DequeList()

    def push(self,info):
        self.infos.insertLast(info)

    def pop(self):
        return self.infos.removeLast()

    def peek(self):
        return self.infos.tail.info

    def size(self):
        return self.infos.size

    def isEmpty(self):
        return self.infos.isEmpty()

    def __iter__(self):
        return self.infos.__iter__()

    def __next__(self):
        return self.infos.__next__()

    def clear(self):
        self.infos.clear()

