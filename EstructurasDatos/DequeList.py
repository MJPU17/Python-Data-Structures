from DNode import DNode
from MyDoubleLinkedList import MyDoubleLinkedList

class DequeList(MyDoubleLinkedList):

    def __init__(self):
        super().__init__()
        self.tail=DNode()
        self.head=DNode()
        self.head.next=self.tail
        self.tail.previous=self.head

    def insertLast(self, info):
        t=self.tail
        temp=DNode(info)
        temp.previous=t
        t.next=temp
        self.current=temp
        self.tail=temp
        if self.size==0:
            self.head=temp
        self.size+=1
        self.position=self.size-1

    def removeLast(self):
        value=None
        if self.tail is None:
            return value
        value=self.tail.info
        self.tail=self.tail.previous
        if self.tail is not None:
            self.tail.next=None
        self.size-=1
        self.position=self.size-1
        self.current=self.tail
        if self.size==0:
            self.tail = DNode()
            self.head = DNode()
            self.head.next = self.tail
            self.tail.previous = self.head
        return value

    def insertFirst(self,info):
        h=self.head
        temp=DNode(info)
        temp.next=h
        h.previous=temp
        self.current=temp
        self.head=temp
        if self.size==0:
            self.tail=temp
        self.size+=1
        self.position=0

    def removeFirst(self):
        value=None
        if self.head is None:
            return value
        value=self.head.info
        self.head=self.head.next
        if self.head is not None:
            self.head.previous=None
        self.size-=1
        self.position=0
        self.current=self.head
        if self.size==0:
            self.tail = DNode()
            self.head = DNode()
            self.head.next = self.tail
            self.tail.previous = self.head
        return value


