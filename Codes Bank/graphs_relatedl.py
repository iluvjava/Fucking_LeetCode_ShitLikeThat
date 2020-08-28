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




