from Node import Node

class MyLinkedList:

    def __init__(self):
        self.first=None
        self.size=0

    def isEmpty(self):
        return self.size==0

    def add(self, info):
        newNode = Node(info,self.first)
        self.first = newNode
        self.size+=1

    def getLast(self):
        current = self.first
        while not self.isEmpty() and current.next is not None:
            current = current.next
        return current

    def addLast(self, info):
        newNode = Node(info)
        if self.isEmpty():
            self.first = newNode
        else:
            self.getLast().next=newNode
        self.size+=1

    def getNode(self, n):
        current=self.first
        count=0
        if n<0 or n>=self.size:
            raise IndexError(n)
        while not self.isEmpty() and count<n:
            current=current.next
            count+=1
        return current

    def get(self, n):
        if n<0 or n>=self.size:
            raise IndexError(n)
        return self.getNode(n).info

    def remove(self, n):
        if n<0 or n>=self.size:
            raise IndexError(n)
        if n==0:
            if self.first.next is not None:
                self.first=self.first.next
            else:
                self.first=None
        else:
            self.getNode(n-1).next=self.getNode(n).next
        self.size-=1

    def set(self, n, info):
        if n<0 or n>=self.size:
            raise IndexError(n)
        self.getNode(n).info=info

    def clear(self):
        while not  self.isEmpty():
            self.remove(0)

    def __iter__(self):
        self.current=self.first
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            info=self.current.info
            self.current=self.current.next
            return info
