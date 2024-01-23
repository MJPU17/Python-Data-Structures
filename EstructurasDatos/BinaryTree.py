from TNode import TNode
from MyLinkedList import MyLinkedList

class BinaryTree:

    def __init__(self):
        self.root=None
        self.route=MyLinkedList()

    def insertRec(self, root, key):
        if root is None:
            root=TNode(key)
            return root
        if key<=root.key:
            root.left=self.insertRec(root.left,key)
        elif key>root.key:
            root.right=self.insertRec(root.right,key)
        return root

    def insert(self, key):
        self.root=self.insertRec(self.root, key)

    def inOrderRec(self, root):
        if root is not None:
            self.inOrderRec(root.left)
            self.route.addLast(root.key)
            self.inOrderRec(root.right)

    def postOrderRec(self, root):
        if root is not None:
            self.postOrderRec(root.left)
            self.postOrderRec(root.right)
            self.route.addLast(root.key)

    def preOrderRec(self, root):
        if root is not None:
            self.route.addLast(root.key)
            self.preOrderRec(root.left)
            self.preOrderRec(root.right)

    def inOrder(self):
        self.route.clear()
        self.inOrderRec(self.root)
        return self.route

    def preOrder(self):
        self.route.clear()
        self.preOrderRec(self.root)
        return self.route

    def postOrder(self):
        self.route.clear()
        self.postOrderRec(self.root)
        return self.route

    def removeLeaves(self, root):
        if root is not None:
            self.removeLeaves(root.left)
            self.removeLeaves(root.right)
            root = None

    def clear(self):
        self.removeLeaves(self.root)
        self.root = None
        self.route.clear()

