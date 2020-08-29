

def dfs_modified(v, adjList, colorDict, targetColor):
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
    Visited = set()
    Distance = 0
    while len(Q) != 0:
        U = Q.pop(0)
        if U == 0:
            continue # Discolored vertex should be skipped. 
        if colorDict[U] == targetColor and U != v:
            return Distance, U
        for W in adjList[U]:
            if not (W in Visited): 
                Visited.add(W)
                Q.append(W)
        Visited.add(U)
        Distance += 1
    return None, None


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    """
        GRAPH INDEXED STARTING FROM 1
    """
    if val not in ids:
        return -1
    # make adj list and color table --------------------------------------------
    AjdList = dict((I + 1, []) for I in range(graph_nodes))
    for V, U in zip(graph_from, graph_to):
        AjdList[V].append(U)
        AjdList[U].append(V)
    del U, V
    # index starts with 1. color zero is a color to ignore. --------------------
    ColorDict = dict((I + 1, V) for I, V in enumerate(ids))
    VertexWithThatColor = [ID for ID, C in ColorDict.items() if C == val]
    MinDis = float("+inf")
    while len(VertexWithThatColor) >= 0:
        V = VertexWithThatColor.pop()
        Distance, NextVertex = dfs_modified(V, AjdList, ColorDict, val)
        if NextVertex is None: 
            # Queue must be empty at this point. 
            break
        MinDis = min(MinDis, Distance)
        ColorDict[V] = 0  # No color they already found.
    return MinDis if MinDis != float("+inf") else -1



def main():

    def Test1():
        From = [1, 2, 3, 4]
        To = [2, 3, 4, 5]
        Colors = [1, 2, 2, 2, 1]
        Val = 1
        print(findShortest(5, From, To, Colors, Val))
    
    Test1()
    pass



if __name__ == "__main__":
    main()