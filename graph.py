import Queue
from linkedList import LinkedList


class Graph:
    """
        This class will always take a list of pairs to represent the graph. We will try to build
        an adjacency list, run dfs, run bfs, and also an adjacency matrix
        eg. edges =
        [
            (1, 2), (2, 3), (3, 4), (4, 5), (5, 1),
            (1, 6), (6, 7), (7, 8), (8, 9), (9, 1),
            (3, 7), (5, 9), (6, 4), (2, 8)
        ]

    """
    GraphList: list
    AdjacencyList: dict

    def __init__(self, graphList):
        # The input will be a list in this format [[Node, Node], [Node, Node]]  where the connection is from
        # index 0->1
        self.GraphList = graphList
        self.AdjacencyList = None

    def buildAdjacencyList(self):
        """
        An adjacency list is a list of linked lists containing the nodes.
        :return:
        """
        if self.AdjacencyList is not None:
            return self.AdjacencyList
        adjacencyMap = {}
        for connections in self.GraphList:
            fromNode = str(connections[0])
            toNode = str(connections[1])
            if adjacencyMap.get(fromNode) is None:
                # Map has not been initialised at all. Init a new LL for node
                newList = LinkedList()
                newList.initList(toNode)
                adjacencyMap[fromNode] = newList
            else:
                # Iterate till the end of the list and attach this new value
                nodeList: LinkedList = adjacencyMap.get(fromNode)
                nodeList.addValue(toNode)
        # Finished building list
        self.AdjacencyList = adjacencyMap
        return self.AdjacencyList

    @staticmethod
    def printAdjacencyList(adjacencyList: dict):
        keys = list(adjacencyList.keys())
        for key in keys:
            print(f"For node {key} the connections are:")
            ll: LinkedList | None = adjacencyList.get(key)
            if ll is None:
                print("No connections present for this node")
            else:
                valueList = ll.getListOfValues()
                print(f"\t{'->'.join(valueList)}")

    def bfs(self):
        """
        We need to use a queue to fill up
        :return:
        """
        q = Queue.DynamicQueue()
        al = self.buildAdjacencyList()
        nodes = list(al.keys())
        if len(nodes) == 0:
            print("BFS stopped. Graph is empty.")
            return
        visited = {}
        q.enqueue(nodes[0])
        while not q.is_empty():
            curr = q.dequeue()
            visited[curr] = True
            print(f"Current level is {curr}")
            ll: LinkedList = al.get(curr)
            if ll is None:
                print("No connections.")
            else:
                neighbours = ll.getListOfValues()
                for neighbour in neighbours:
                    print(f"\t{neighbour} is on this level")
                    if visited.get(neighbour) is None:
                        visited[neighbour] = True
                        q.enqueue(neighbour)
        print("BFS completed")

    def dfs(self):
        """
        We will be using a stack to implement dfs
        :return:
        """
        stack = []
        al = self.buildAdjacencyList()
        nodes = list(al.keys())
        if len(nodes) == 0:
            print("DFS stopped. Graph is empty.")
            return
        visited = {}
        stack.append(nodes[0])
        while len(stack) > 0:
            curr = stack.pop()
            print(f"Going deep in {curr}")
            visited[curr] = True
            ll: LinkedList = al[curr]
            if ll is None:
                print("No connection")
            else:
                neighbours = ll.getListOfValues()
                for neighbour in neighbours:
                    print(f"\tVisited {neighbour}")
                    if visited.get(neighbour) is None:
                        stack.append(neighbour)

        print("DFS completed.")