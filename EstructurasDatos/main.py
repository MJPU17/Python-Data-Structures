from MyLinkedList import MyLinkedList
from MyDoubleLinkedList import MyDoubleLinkedList
from DequeList import DequeList
from QueueImp import QueueImp
from StackImp import StackImp
from MyMap import MyMap
from MyGraph import MyGraph
from BreadthFirstSearch import BreadthFirstSearch
from DeepFirstSearch import DeepFirstSearch
from BellmanFord import BellmanFord
from Dijkstra import Dijkstra
from BinaryTree import BinaryTree
from GenericTree import GenericTree

def linkedList():
    list=MyLinkedList()
    for i in range(100,121):
        list.addLast(i)
    for aux in list:
        print(aux,end=" ")
    list.remove(0)
    print()
    for aux in list:
        print(aux, end=" ")
    list.remove(list.size-1)
    print()
    for aux in list:
        print(aux, end=" ")
    list.remove(5)
    list.remove(0)
    list.remove(2)
    print()
    for aux in list:
        print(aux,end=" ")
    while not list.isEmpty():
        list.remove(0)
    for i in range(200,223):
        list.addLast(i)
    print()
    for aux in list:
        print(aux,end=" ")
    list.clear()
    print("\nSize: ",list.size,sep="")
    for aux in list:
        print(aux,end=" ")
    for i in range(223,244):
        list.addLast(i)
    print("\nSize: ", list.size, sep="")
    list.set(2,1234)
    list.set(0,1345)
    list.set(list.size-1,2367)
    for aux in list:
        print(aux,end=" ")

def doubleLinkedList():
    dlist=MyDoubleLinkedList()
    for i in range(5):
        dlist.add(i)
    for i in range(dlist.size):
        print(dlist.get(i),end=" ")
    print()
    dlist.remove(3)
    for i in range(dlist.size):
        print(dlist.get(i),end=" ")
    print()
    dlist.remove(3)
    for i in range(dlist.size):
        print(dlist.get(i),end=" ")
    print()
    dlist.addIndex(1,100)
    for i in range(dlist.size):
        print(dlist.get(i),end=" ")
    print()
    dlist.addInit(345)
    for i in range(dlist.size):
        print(dlist.get(i),end=" ")
    print()
    dlist.remove(0)
    for aux in dlist:
        print(aux,end=" ")
    print()
    dlist.remove(dlist.size-1)
    for aux in dlist:
        print(aux, end=" ")
    print()
    while not dlist.isEmpty():
        dlist.remove(0)
    for i in range(90,121):
        dlist.add(i)
    for aux in dlist:
        print(aux, end=" ")
    print()
    dlist.clear()
    print("Size: ",dlist.size,sep="")
    for aux in dlist:
        print(aux, end=" ")
    print()
    for i in range(121,141):
        dlist.add(i)
    dlist.set(2,1234)
    dlist.set(0,1345)
    dlist.set(dlist.size-1,2367)
    print("Size: ",dlist.size,sep="")
    for aux in dlist:
        print(aux, end=" ")

def dequeList():
    dqlist=DequeList()
    for i in range(1,11):
        if i%2==0:
            dqlist.insertFirst(i)
        else:
            dqlist.insertLast(i)
    for i in range(dqlist.size):
        print(dqlist.get(i),end=" ")
    print()
    dqlist.removeFirst()
    dqlist.removeLast()
    for i in range(dqlist.size):
        print(dqlist.get(i),end=" ")
    print()
    dqlist.removeFirst()
    dqlist.removeLast()
    for i in range(dqlist.size):
        print(dqlist.get(i),end=" ")
    print("\n",dqlist.tail.info,sep="")
    while not dqlist.isEmpty():
        print(dqlist.removeLast(),end=" ")
    print()
    print(dqlist.tail is None)
    print(dqlist.tail is None)
    for i in range(30,47):
        if i%2==0:
            dqlist.insertLast(i)
        else:
            dqlist.insertFirst(i)
    for aux in dqlist:
        print(aux,end=" ")
    dqlist.clear()
    print("\nSize: ", dqlist.size, sep="")
    for aux in dqlist:
        print(aux,end=" ")
    for i in range(47,77):
        if i%2==0:
            dqlist.insertFirst(i)
        else:
            dqlist.insertLast(i)
    print("\nSize: ", dqlist.size, sep="")
    for aux in dqlist:
        print(aux,end=" ")

def queue():
    queue=QueueImp()
    for i in range(ord('A'),ord('Z')+1):
        queue.enqueue(chr(i))
    for aux in queue:
        print(aux,end=" ")
    print()
    queue.dequeue()
    for aux in queue:
        print(aux,end=" ")
    print("\n",queue.peek(),sep="")
    while not queue.isEmpty():
        print(queue.dequeue(),end=" ")
    print()
    for i in range(ord('a'),ord('z')+1):
        queue.enqueue(chr(i))
    for aux in queue:
        print(aux,end=" ")
    print()
    queue.clear()
    print("Size: ",queue.size(),sep="")
    for aux in queue:
        print(aux,end=" ")
    print()
    for i in range(ord('z'),ord('a')-1,-1):
        queue.enqueue(chr(i))
    print("Size: ",queue.size(),sep="")
    while not queue.isEmpty():
        print(queue.dequeue(),end=" ")
    print()

def stack():
    stack=StackImp()
    for i in range(ord('A'),ord('Z')+1):
        stack.push(chr(i))
    for aux in stack:
        print(aux,end=" ")
    print()
    stack.pop()
    for aux in stack:
        print(aux,end=" ")
    print("\n",stack.peek(),sep="")
    while not stack.isEmpty():
        print(stack.pop(),end=" ")
    print()
    for i in range(ord('a'),ord('z')+1):
        stack.push(chr(i))
    for aux in stack:
        print(aux,end=" ")
    print()
    stack.clear()
    print("Size: ",stack.size(),sep="")
    for aux in stack:
        print(aux,end=" ")
    print()
    for i in range(ord('z'),ord('a')-1,-1):
        stack.push(chr(i))
    print("Size: ", stack.size(), sep="")
    for aux in stack:
        print(aux,end=" ")
    print()
    while not stack.isEmpty():
        print(stack.pop(),end=" ")

def map():
    map=MyMap()
    for i in range(ord('A'),ord('M')+1):
        map.put(chr(i),i)
    for aux in map.keySet():
        print(aux,": ",map.getValue(aux),sep="")
    print()
    for i in range(ord('A'),ord('M')+1):
        print(chr(i),": ",map.getValue((chr(i))),sep="")
    print()
    for i in range(ord('A'),ord('Z')+1):
        if map.containsKey(chr(i)):
            print(chr(i),": True")
        else:
            print(chr(i), ": False")
    print()
    for i in range(ord('A'),ord('Z')+1):
        if i<=ord('M'):
            map.remove(chr(i))
        else:
            map.put(chr(i),i)
    for aux in map.keySet():
        print(aux,": ",map.getValue(aux),sep="")
    print()
    j=1
    for i in range(ord('N'),ord('Z')+1):
        map.replace(chr(i),j)
        j+=1
    for aux in map.keySet():
        print(aux,": ",map.getValue(aux),sep="")
    print()
    for i in range(ord('N'),ord('Z')+1):
        j-=1
        map.put(chr(i),j)
    for aux in map.keySet():
        print(aux,": ",map.getValue(aux),sep="")
    print()
    map.clear()
    print("Size: ",map.size,sep="")
    for aux in map.keySet():
        print(aux,": ",map.getValue(aux),sep="")
    print()
    map.put('V',22)
    print("Size: ", map.size, sep="")
    for aux in map.keySet():
        print(aux, ": ", map.getValue(aux), sep="")

def graph():
    graph=MyGraph()
    graph.addNode("Bogota")
    graph.addNode("Cali")
    graph.addNode("Cartagena")
    graph.addEdge("Cali", "Bogota", 19)
    graph.addEdge("Bogota", "Cartagena", 32)
    graph.addEdge("Cartagena", "Cali", 8)
    graph.addEdge("Cali", "Cartagena", 3)
    graph.addEdge("Cartagena", "Bogota", 5)
    for i in range(graph.numNodes):
        print(graph.numberToNode(i),": ",sep=" ")
        for j in range(graph.adj.get(i).size):
            n=graph.adj.get(i).get(j)
            print("[",graph.numberToNode(n.number),", ",n.weigth,"]",sep="",end=" ")
        print()

def bfs():
    graph=MyGraph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addNode('D')
    graph.addNode('F')
    graph.addEdge('A', 'B', 1)
    graph.addEdge('A', 'C', 1)
    graph.addEdge('B', 'D', 1)
    graph.addEdge('B', 'F', 1)
    graph.addEdge('D', 'C', 1)
    graph.addEdge('D', 'F', 1)
    graph.addEdge('F', 'A', 1)

    source='B'

    bfs=BreadthFirstSearch(graph,source)
    bfs.runSearch()
    for i in range(graph.numNodes):
        destination=graph.numberToNode(i)
        if bfs.obtainDistance(destination)!=-1:
            print("El camino mas corto del nodo ",source," al ",destination," es:",sep="")
            way=""
            current=i
            while current!=-1:
                way=graph.numberToNode(current)+" "+way
                current=bfs.previous.get(current)
            print("Camino:",way)
            print("Distancia: ",bfs.obtainDistance(destination),end="\n\n",sep="")
        else:
            print("No hay camino del nodo ", source, " al ", destination, ".", sep="")

def dfs():
    graph=MyGraph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addNode('D')
    graph.addNode('F')
    graph.addNode('G')
    graph.addNode('H')
    graph.addNode('I')
    graph.addNode('J')
    graph.addNode('M')
    graph.addEdge('A', 'B', 1)
    graph.addEdge('A', 'D', 1)
    graph.addEdge('A', 'C', 1)
    graph.addEdge('B', 'G', 1)
    graph.addEdge('B', 'F', 1)
    graph.addEdge('D', 'J', 1)
    graph.addEdge('D', 'M', 1)
    graph.addEdge('F', 'H', 1)
    graph.addEdge('F', 'I', 1)

    source='B'

    dfs=DeepFirstSearch(graph,source)
    dfs.runSearch()

    for i in range(graph.numNodes):
        node=graph.numberToNode(i)
        if dfs.obtainDiscover(node)!=0:
            print("Tiempo descubrimiento nodo ",node,": ",dfs.obtainDiscover(node),sep="")
            print("Tiempo terminacion nodo ", node, ": ", dfs.obtainTermination(node), sep="",end="\n\n")
        else:
            print("No se puede llegar desde el origen ",source," a ",node,".",sep="",end="\n\n")

def bellmanFord():
    graph=MyGraph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addNode('D')
    graph.addNode('E')
    graph.addNode('F')
    graph.addEdge('A', 'B', 3)
    graph.addEdge('A', 'F', 40)
    graph.addEdge('B', 'E', 3)
    graph.addEdge('B', 'D', 15)
    graph.addEdge('D', 'E', 20)
    graph.addEdge('F', 'C', -3)

    source='B'

    bf=BellmanFord(graph, source)
    bf.initBellmanFord()
    if bf.negativeCicle:
        print("Hay ciclo.")
    else:
        for i in range(graph.numNodes):
            destination=graph.numberToNode(i)
            if bf.isPath(destination):
                current=i
                way=""
                while current!=-1:
                    way=graph.numberToNode(current)+" "+way
                    current=bf.previous.get(current)
                print("El camino mas corto del nodo ",source," al ",destination," es:",sep="")
                print(way)
                print("Distancia: ",bf.obtainDistance(destination),end="\n\n",sep="")
            else:
                print("No hay camino del nodo ",source, " al ", destination,".",end="\n\n",sep="")

def bellmanFord2():
    graph=MyGraph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addEdge('A', 'B', -1)
    graph.addEdge('B', 'C', 1)
    graph.addEdge('C', 'A', -1)

    source='A'
    bf = BellmanFord(graph, source)
    bf.initBellmanFord()
    if bf.negativeCicle:
        print("Hay ciclo.")
    else:
        for i in range(graph.numNodes):
            destination = graph.numberToNode(i)
            if bf.isPath(destination):
                current = i
                way = ""
                while current != -1:
                    way = graph.numberToNode(current) + " " + way
                    current = bf.previous.get(current)
                print("El camino mas corto del nodo ", source, " al ", destination, " es:", sep="")
                print(way)
                print("Distancia: ", bf.obtainDistance(destination), end="\n\n", sep="")
            else:
                print("No hay camino del nodo ", source, " al ", destination, ".", end="\n\n", sep="")

def dijkstra():
    graph=MyGraph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addNode('D')
    graph.addNode('E')
    graph.addNode('F')
    graph.addNode('G')
    graph.addNode('H')
    graph.addNode('I')
    graph.addNode('J')
    graph.addNode('K')
    graph.addNode('L')
    graph.addNode('M')
    graph.addNode('N')
    graph.addNode('P')
    graph.addEdge('A', 'B', 8)
    graph.addEdge('A', 'D', 5)
    graph.addEdge('A', 'E', 4)
    graph.addEdge('B', 'C', 3)
    graph.addEdge('B', 'F', 4)
    graph.addEdge('B', 'E', 12)
    graph.addEdge('D', 'E', 9)
    graph.addEdge('D', 'H', 6)
    graph.addEdge('F', 'G', 1)
    graph.addEdge('F', 'K', 8)
    graph.addEdge('F', 'E', 3)
    graph.addEdge('E', 'J', 5)
    graph.addEdge('E', 'I', 8)
    graph.addEdge('H', 'I', 2)
    graph.addEdge('H', 'M', 7)
    graph.addEdge('G', 'L', 7)
    graph.addEdge('G', 'K', 8)
    graph.addEdge('K', 'L', 5)
    graph.addEdge('K', 'P', 7)
    graph.addEdge('K', 'J', 6)
    graph.addEdge('J', 'N', 9)
    graph.addEdge('J', 'I', 10)
    graph.addEdge('I', 'M', 6)
    graph.addEdge('L', 'P', 6)
    graph.addEdge('P', 'N', 17)
    graph.addEdge('N', 'M', 2)

    source='B'

    dj=Dijkstra(graph,source)
    dj.runDijkstra()

    for i in range(graph.numNodes):
        destination = graph.numberToNode(i)
        if dj.isPath(destination):
            current = i
            way = ""
            while current != -1:
                way = graph.numberToNode(current) + " " + way
                current = dj.previous.get(current)
            print("El camino mas corto del nodo ", source, " al ", destination, " es:", sep="")
            print(way)
            print("Distancia: ", dj.obtainDistance(destination), end="\n\n", sep="")
        else:
            print("No hay camino del nodo ", source, " al ", destination, ".", end="\n\n", sep="")

def binaryTree():
    bt=BinaryTree()
    bt.insert('C')
    bt.insert('F')
    bt.insert('B')
    bt.insert('D')
    bt.insert('A')

    print("Caracteres:")
    print("Inorder: ",end="")
    for aux in bt.inOrder():
        print(aux,end=" ")
    print("\nPostorder: ",end="")
    for aux in bt.postOrder():
        print(aux,end=" ")
    print("\nPreorder: ",end="")
    for aux in bt.preOrder():
        print(aux,end=" ")
    print()
    bt.clear()


    bt2=BinaryTree()
    bt2.insert(5)
    bt2.insert(4)
    bt2.insert(7)
    bt2.insert(2)
    bt2.insert(11)
    print("\nNumeros:")
    print("Inorder: ", end="")
    for aux in bt2.inOrder():
        print(aux, end=" ")
    print("\nPostorder: ", end="")
    for aux in bt2.postOrder():
        print(aux, end=" ")
    print("\nPreorder: ", end="")
    for aux in bt2.preOrder():
        print(aux, end=" ")
    print()
    bt2.clear()

    bt3=BinaryTree()
    bt3.insert("AC")
    bt3.insert("AD")
    bt3.insert("AF")
    bt3.insert("AA")
    bt3.insert("AE")

    print("\nString:")
    print("Inorder: ", end="")
    for aux in bt3.inOrder():
        print(aux, end=" ")
    print("\nPostorder: ", end="")
    for aux in bt3.postOrder():
        print(aux, end=" ")
    print("\nPreorder: ", end="")
    for aux in bt3.preOrder():
        print(aux, end=" ")
    print()

def genericTree():
    gt=GenericTree()
    gt.addRoot("A")
    gt.addNode("A", "B")
    gt.addNode("A", "C")
    gt.addNode("A", "D")
    gt.addNode("B", "E")
    gt.addNode("B", "F")
    gt.addNode("D", "G")
    gt.addNode("D", "H")
    gt.addNode("D", "I")
    gt.levelOrder(gt.root)
    print("Level Order:")
    for aux in gt.levels.keySet():
        print("Level:", aux)
        for leave in gt.levels.getValue(aux):
            print(leave, end=" ")
        print("\n")
    print("PreOrder:")
    for aux in gt.preOrder(gt.root):
        print(aux, end=" ")
    print("\nPostOrder:")
    for aux in gt.postOrder(gt.root):
        print(aux, end=" ")
    gt.clear()
    gt.addRoot("a")
    gt.addNode("a", "b")
    gt.addNode("a", "c")
    gt.addNode("a", "d")
    gt.addNode("b", "e")
    gt.addNode("b", "f")
    gt.addNode("d", "g")
    gt.addNode("d", "h")
    gt.addNode("d", "i")
    gt.levelOrder(gt.root)
    print("\n\nLevel Order:")
    for aux in gt.levels.keySet():
        print("Level:", aux)
        for leave in gt.levels.getValue(aux):
            print(leave, end=" ")
        print("\n")
    print("PreOrder:")
    for aux in gt.preOrder(gt.root):
        print(aux, end=" ")
    print("\nPostOrder:")
    for aux in gt.postOrder(gt.root):
        print(aux, end=" ")


genericTree()
