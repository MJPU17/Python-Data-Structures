from MyLinkedList import MyLinkedList
from QueueImp import QueueImp

class BreadthFirstSearch:

    def __init__(self, graph=None, source=None):
        self.graph=graph
        self.source=source
        self.distance=MyLinkedList()
        self.previous=MyLinkedList()
        for i in range(graph.numNodes):
            self.distance.add(-1)
            self.previous.add(-1)

    def init(self):
        for i in range(self.graph.numNodes):
            self.distance.set(i,-1)
            self.previous.set(i,-1)

    def runSearch(self):
        self.init()
        queue=QueueImp()
        self.distance.set(self.graph.nodeToNumber(self.source),0)
        queue.enqueue(self.graph.nodeToNumber(self.source))
        while not queue.isEmpty():
            u=queue.dequeue()
            for v in self.graph.adj.get(u):
                if self.distance.get(v.number)==-1:
                    self.distance.set(v.number,self.distance.get(u)+1)
                    self.previous.set(v.number,u)
                    queue.enqueue(v.number)

    def obtainDistance(self, destination):
        return self.distance.get(self.graph.nodeToNumber(destination))

    def obtainPrevious(self, node):
        n = self.graph.nodeToNumber(node)
        return self.graph.numberToNode(self.previous.get(n))

    def clear(self):
        self.distance.clear()
        self.previous.clear()

