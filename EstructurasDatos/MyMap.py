from MNode import MNode
from MyLinkedList import MyLinkedList

class MyMap:

    def __init__(self):
        self.size=0
        self.first=None

    def isEmpty(self):
        return self.size==0

    def keySet(self):
        keys=MyLinkedList()
        current=self.first
        while current is not None:
            keys.addLast(current.key)
            current=current.next
        return keys

    def values(self):
        values=MyLinkedList()
        current=self.first
        while current is not None:
            values.addLast(current.info)
            current=current.next
        return values

    def containsKey(self, key):
        current=self.first
        while current is not None:
            if current.key==key:
                return True
            current=current.next
        return False

    def put(self, key, info):
        newNode=MNode(key, info)
        if self.first is None:
            self.first=newNode
        else:
            current=self.first
            while current.next is not None:
                if current.key==key:
                    current.info=info
                    return
                current=current.next
            if current.key == key:
                current.info = info
                return
            current.next=newNode
        self.size+=1

    def replace(self, key, info):
        current=self.first
        while current is not None:
            if current.key==key:
                current.info=info
                return True
            current=current.next
        return False

    def remove(self, key):
        if self.first.key==key:
            self.first=self.first.next
            self.size-=1
        else:
            current=self.first
            while current.next is not None:
                if current.next.key==key:
                    self.size-=1
                    current.next=current.next.next;
                    return True
                current=current.next
        return False

    def getValue(self, key):
        current=self.first
        while current is not None:
            if current.key==key:
                return current.info
            current=current.next
        return None

    def clear(self):
        while not self.isEmpty():
            self.remove(self.first.key)

