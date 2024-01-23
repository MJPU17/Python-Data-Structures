from Vertex import Vertex
from MyDoubleLinkedList import MyDoubleLinkedList
from MyMap import MyMap

class MyGraph:

    def __init__(self):
        self.numNodes=0
        self.numEdges=0
        self.traduct=MyMap()
        self.inverseTraduct=MyMap()
        self.adj=MyDoubleLinkedList()

    def addNode(self, node):
        self.traduct.put(node, self.numNodes)
        self.inverseTraduct.put(self.numNodes, node)
        self.adj.add(MyDoubleLinkedList())
        self.numNodes+=1

    def addEdge(self, source, destination, weigth):
        self.adj.get(self.traduct.getValue(source)).add(Vertex(self.traduct.getValue(destination),weigth))
        self.numEdges+=1

    def nodeToNumber(self, node):
        if self.traduct.containsKey(node):
            return  self.traduct.getValue(node)
        return -1

    def numberToNode(self, node):
        return self.inverseTraduct.getValue(node)

    def clear(self):
        self.numNodes=0
        self.numEdges=0
        self.traduct.clear()
        self.inverseTraduct.clear()
        self.adj.clear()

