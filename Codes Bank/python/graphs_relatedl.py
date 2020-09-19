def dfs(v, adjList):
    """
        provide a vertex and an adjacency list, provide a vertex that is in 
        the adjacency list.

        * The graph is assumed to be a simple Digraph, for undirected graph,
        we need double edges, and that is allowed. 

        The adjacency list is represented by a list 
        {
            int |---> List[int]
        }

        * Skip self edges. 
    :return:    
        A set of vertices that has been reached by the DFS from that starting 
        vertext v. 
    """
    Q = [v]
    V = set()
    while len(Q) != 0:
        U = Q.pop(0)
        for W in adjList[U]:
            if (W not in V):
                V.add(W)
        V.add(U)
    else:
        V.add(v)
    return V


def to_adjlist(edges):
    """
        Edges are a list list, it assume that the graph undirected 
        returns the adjacency list of the graph
    """
    AdjList = {}
    for L in edges: 
        [U, V] = L
        UNeighbours = AdjList.get(U, [])
        VNeighbours = AdjList.get(V, [])
        UNeighbours.append(V)
        VNeighbours.append(U)
        AdjList[U] = UNeighbours
        AdjList[V] = VNeighbours
    print(f"Adjlist: {AdjList}")
    return AdjList


def get_dfs_tree(startingVertex, adjList):
    """
        Given a Adjacency list this function will return another adjlist that represents
        the DFS tree of the given graph. 
    """
    AdjListDFS = {}
    Stack = [startingVertex]
    Visited = set(); Visited.add(startingVertex)
    while len(Stack) != 0:
        U = Stack.pop()
        for V in adjList[U]:
            if V not in Visited:
                NeighboursList = AdjListDFS.get(U, [])
                NeighboursList.append(V)
                AdjListDFS[U] = NeighboursList
                Visited.add(V)
                Stack.append(V)
    return AdjListDFS


def main():
    def Test1():
        Edges = [
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 1]
        ]
        print(to_adjlist(Edges))
    
    def Test2():
        EdgeList = [
            [1, 2],
            [2, 4],
            [2, 5],
            [1, 3],
            [3, 6],
            [3, 7],
            [1, 7],
            [1, 4]
        ]
        AdjList = to_adjlist(EdgeList)
        print("DFS Tree: ")
        print(get_dfs_tree(1, AdjList))

    Test1()
    Test2()


if __name__ == "__main__":
    main()