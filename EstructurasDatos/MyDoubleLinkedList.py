from DNode import DNode

class MyDoubleLinkedList:

    def __init__(self):
        self.position=-1
        self.size=0
        self.head=None
        self.current=None

    def isEmpty(self):
        return self.size==0

    def forward(self, numposition):
        if numposition>0 and self.head is not None:
            positionForward=numposition
            if self.current is None:
                self.current=self.head
                positionForward-=1
                self.position+=1
            while self.current.next is not None and positionForward>0:
                self.current=self.current.next
                positionForward-=1
                self.position+=1

    def backward(self, numposition):
        if numposition<=0 or self.head is None or self.current is None:
            return
        positionBackward=numposition
        while self.current is not None and positionBackward>0:
            self.current=self.current.previous
            positionBackward-=1
            self.position-=1

    def insert(self,info):
        temp=DNode(info)
        if self.current is None:
            temp.next=self.head
            if self.head is not None :
                self.head.previous=temp
            self.head=temp
        else:
            temp.next=self.current.next
            temp.previous=self.current
            if self.current.next is not None:
                self.current.next.previous=temp
            self.current.next=temp
        self.current=temp
        self.position+=1
        self.size+=1

    def extract(self):
        info=None
        if self.current is not None:
            info=self.current.info
            if self.head==self.current and self.position==0:
                self.head=self.current.next
            else:
                self.current.previous.next=self.current.next
            if self.current.next is not None:
                self.current.next.previous=self.current.previous
            self.current=self.current.next
            if self.size-1==self.position:
                self.position=-1
            self.size-=1
        return info

    def remove(self, index):
        if self.position>index:
            self.backward(abs(self.position-index))
        else:
            self.forward(abs(self.position-index))
        return self.extract()

    def addInit(self,info):
        self.backward(self.size)
        self.insert(info)

    def add(self,info):
        self.forward(self.size)
        self.insert(info)

    def addIndex(self, index, info):
        index-=1
        if self.position>index:
            self.backward(abs(self.position-index))
        else:
            self.forward(abs(self.position-index))
        self.insert(info)

    def get(self,index):
        if self.position>index:
            self.backward(abs(self.position-index))
        else:
            self.forward(abs(self.position-index))
        return self.current.info

    def set(self, index, info):
        if self.position>index:
            self.backward(abs(self.position-index))
        else:
            self.forward(abs(self.position-index))
        self.current.info=info

    def clear(self):
        while not  self.isEmpty():
            self.remove(0)

    def __iter__(self):
        self.node=self.head
        return self

    def __next__(self):
        if self.node is None:
            raise StopIteration
        else:
            info=self.node.info
            self.node=self.node.next
            return info

