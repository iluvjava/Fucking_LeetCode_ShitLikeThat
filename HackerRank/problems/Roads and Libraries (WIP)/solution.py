
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


def solution(n, c_lib, c_road, cities):
    """
        cities in the format of: 
        [[v1, v2], [v1, v3], [,]... []]

        Vertex starts indexing from 1.
    """
    if c_lib <= c_road:
        return c_lib * n
    # Get the Adjacency list ---------------------------------------------------
    AjdList = dict((I, []) for I in range(n))
    for V, U in cities:
        AjdList[V - 1].append(U - 1)
        AjdList[U - 1].append(V - 1)
    # Get the size for all connected components in the graph -------------------
    Explored = set()
    CCSize = []
    for V in range(n):
        if V in Explored:
            continue
        CC = dfs(V, AjdList)
        Explored = Explored.union(CC)
        CCSize.append(len(CC))
    # Computing the total Costs ------------------------------------------------
    return sum(((K - 1)*c_road + c_lib) for K in CCSize)


def main():
    cities = [[1, 2], [1, 3], [1, 4]]
    print(solution(5, 6, 1, cities))


if __name__ == "__main__":
    main()
