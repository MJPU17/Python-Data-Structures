from MyLinkedList import MyLinkedList

class BellmanFord:

    def __init__(self, graph=None, source=None):
        self.graph=graph
        self.source=source
        self.negativeCicle=False
        self.INF=1 << 30
        self.previous=MyLinkedList()
        self.distance=MyLinkedList()
        for i in range(graph.numNodes):
            self.previous.add(0)
            self.distance.add(0)

    def init(self):
        self.negativeCicle=False
        for i in range(self.graph.numNodes):
            self.previous.set(i,-1)
            self.distance.set(i,self.INF)

    def relaxation(self, current, adjacent, weigth):
        if self.distance.get(current) + weigth < self.distance.get(adjacent):
            self.distance.set(adjacent, self.distance.get(current) + weigth)
            self.previous.set(adjacent,current)
            return True
        return False

    def initBellmanFord(self):
        self.init()
        self.distance.set(self.graph.nodeToNumber(self.source),0)
        for i in range(self.graph.numNodes-1):
            for current in range(self.graph.numNodes):
                for j in range(self.graph.adj.get(current).size):
                    adjacent=self.graph.adj.get(current).get(j).number
                    weigth=self.graph.adj.get(current).get(j).weigth
                    self.relaxation(current,adjacent,weigth)
        for current in range(self.graph.numNodes):
            for j in range(self.graph.adj.get(current).size):
                adjacent = self.graph.adj.get(current).get(j).number
                weigth = self.graph.adj.get(current).get(j).weigth
                if self.relaxation(current, adjacent, weigth):
                    self.negativeCicle=True
                    return

    def obtainDistance(self, destination):
        return self.distance.get(self.graph.nodeToNumber(destination))

    def isPath(self, destination):
        current=self.graph.nodeToNumber(destination)
        while self.previous.get(current)!=-1:
            current=self.previous.get(current)
        return current==self.graph.nodeToNumber(self.source)

    def clear(self):
        self.distance.clear()
        self.previous.clear()

