def solution(n, connections):
    # --------------------------------------------------------------------------
    def ToAdjlist(edges):
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
    
    AdjList = ToAdjlist(connections)

    def GetDFSTree(adjList, startingVertex):
        """
                Given a Adjacency list this function will return another adjlist that represents
                the DFS tree of the given graph. 
            :para startingVertex: 
                This will be the root of the DFSTree
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

    def TreeFindEdges(tree, root, graph):
        ArticulationEdges = []
        
        pass


    pass


def main():
    pass

if __name__ == "__main__":
    main()