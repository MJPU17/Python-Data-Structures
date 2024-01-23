from MyPriorityQueue import MyPriorityQueue
from MyLinkedList import MyLinkedList
from Vertex import Vertex

class Dijkstra:

    def __init__(self, graph=None, source=None):
        self.graph=graph
        self.source=source
        self.pq=MyPriorityQueue()
        self.distance=MyLinkedList()
        self.previous=MyLinkedList()
        self.visited=MyLinkedList()
        self.INF= 1 << 30
        for i in range(graph.numNodes):
            self.previous.add(-1)
            self.distance.add(0)
            self.visited.add(False)

    def init(self):
        for i in range(self.graph.numNodes):
            self.distance.set(i,self.INF)
            self.visited.set(i,False)
            self.previous.set(i,-1)

    def relaxation(self, current, adjacent, weigth):
        if self.distance.get(current) + weigth < self.distance.get(adjacent):
            self.distance.set(adjacent,self.distance.get(current) + weigth)
            self.previous.set(adjacent, current)
            self.pq.insert(Vertex(adjacent, self.distance.get(adjacent)))

    def runDijkstra(self):
        self.init()
        n=self.graph.nodeToNumber(self.source)
        self.pq.insert(Vertex(n,0))
        self.distance.set(n,0)
        while not self.pq.isEmpty():
            current=self.pq.poll().number
            if self.visited.get(current):
                continue
            self.visited.set(current,True)
            for i in range(self.graph.adj.get(current).size):
                adjacent=self.graph.adj.get(current).get(i).number
                weigth=self.graph.adj.get(current).get(i).weigth
                if not self.visited.get(adjacent):
                    self.relaxation(current, adjacent, weigth)

    def obtainDistance(self, destination):
        return self.distance.get(self.graph.nodeToNumber(destination))

    def isPath(self, destination):
        return self.visited.get(self.graph.nodeToNumber(destination))

    def clear(self):
        self.distance.clear()
        self.previous.clear()
        self.visited.clear()

