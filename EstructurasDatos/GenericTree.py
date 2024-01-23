import sys

from GTNode import GTNode
from MyLinkedList import MyLinkedList
from MyMap import MyMap
from QueueImp import QueueImp
from MyDoubleLinkedList import MyDoubleLinkedList

class GenericTree:

    def __init__(self):
        self.root=None
        self.add=False
        self.route=MyLinkedList()
        self.levels=MyMap()

    def searchNodeUtil(self, root, search):
        if root.key == search:
            return root
        for i in range(root.childs.size):
            aux=self.searchNodeUtil(root.childs.get(i),search)
            if aux is not None:
                return aux
        return None

    def searchNode(self, search):
        return self.searchNodeUtil(self.root,search)

    def addChild(self, node, father, child):
        if node.key == father:
            aux=GTNode(child,MyDoubleLinkedList())
            node.childs.add(aux)
            self.add=True
        for i in range(node.childs.size):
            if self.add:
                return
            self.addChild(node.childs.get(i),father,child)

    def addRoot(self, node):
        self.root=GTNode(node,MyDoubleLinkedList())

    def addNode(self, father, child):
        self.add=False
        if self.searchNode(child) is None:
            self.addChild(self.root, father, child)
        return self.add

    def levelOrder(self, root):
        if root is None:
            return
        level=0
        self.route.clear()
        self.levels.clear()
        q=QueueImp()
        q.enqueue(root)
        while not q.isEmpty():
            n=q.size()
            aux=MyLinkedList()
            while n>0:
                current=q.dequeue()
                aux.addLast(current.key)
                for child in current.childs:
                    q.enqueue(child)
                n-=1
            self.levels.put(level,aux)
            level+=1

    def preOrderRec(self, root):
        if root is not None:
            self.route.addLast(root.key)
            for child in root.childs:
                self.preOrderRec(child)

    def postOrderRec(self, root):
        if root is not None:
            for child in root.childs:
                self.postOrderRec(child)
            self.route.addLast(root.key)

    def preOrder(self, root):
        self.route.clear()
        self.preOrderRec(root)
        return self.route

    def postOrder(self, root):
        self.route.clear()
        self.postOrderRec(root)
        return self.route

    def removeLeaves(self, root):
        if root is not None:
            for child in root.childs:
                self.removeLeaves(child)
            root.childs.clear()
            root = None

    def clear(self):
        self.removeLeaves(self.root)
        self.root=None
        self.route.clear()

