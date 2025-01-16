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

    def __init__(self, graphList):
        # The input will be a list in this format [[Node, Node], [Node, Node]]  where the connection is from
        # index 0->1
        self.GraphList = graphList

    def buildAdjacencyList(self):
        """
        An adjacency list is a list of linked lists containing the nodes.
        :return:
        """
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
        return adjacencyMap

    def printAdjacencyList(self, adjacencyList: dict):
        keys = list(adjacencyList.keys())
        for key in keys:
            print(f"For node {key} the connections are:")
            ll: LinkedList | None = adjacencyList.get(key)
            if ll is None:
                print("No connections present for this node")
            else:
                valueList = ll.getListOfValues()
                print("->".join(valueList))

