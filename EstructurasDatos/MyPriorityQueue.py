from MyDoubleLinkedList import MyDoubleLinkedList

class MyPriorityQueue:

    def __init__(self):
        self.datas=MyDoubleLinkedList()

    def insert(self, info):
        for i in range(self.datas.size):
            if self.datas.get(i)>info:
                self.datas.addIndex(i, info)
                return
        self.datas.add(info)

    def poll(self):
        return self.datas.remove(0)

    def size(self):
        return self.datas.size

    def isEmpty(self):
        return self.datas.isEmpty()

    def clear(self):
        self.datas.clear()

