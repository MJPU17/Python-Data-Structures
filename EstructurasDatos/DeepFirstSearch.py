from MyLinkedList import MyLinkedList

class DeepFirstSearch:

    def __init__(self, graph=None, source=None):
        self.graph=graph
        self.source=source
        self.discover=MyLinkedList()
        self.termination=MyLinkedList()
        self.time=0
        for i in range(graph.numNodes):
            self.discover.add(0)
            self.termination.add(0)

    def runSearchUtil(self, u):
        self.discover.set(u,self.time)
        self.time+=1
        for v in self.graph.adj.get(u):
            if self.discover.get(v.number)==0:
                self.runSearchUtil(v.number)
        self.termination.set(u,self.time)
        self.time+=1

    def runSearch(self):
        for i in range(self.graph.numNodes):
            self.discover.set(i,0)
            self.termination.set(i,0)
        self.time=1
        self.runSearchUtil(self.graph.nodeToNumber(self.source))

    def obtainDiscover(self, node):
        return self.discover.get(self.graph.nodeToNumber(node))

    def obtainTermination(self, node):
        return self.termination.get(self.graph.nodeToNumber(node))

    def clear(self):
        self.discover.clear()
        self.termination.clear()

