from graph import Graph

if __name__ == '__main__':

    edges = [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 1),
        (1, 6), (6, 7), (7, 8), (8, 9), (9, 1),
        (3, 7), (5, 9), (6, 4), (2, 8)
    ]
    gh = Graph(edges)
    al = gh.buildAdjacencyList()
    gh.printAdjacencyList(al)
    gh.bfs()
    gh.dfs()