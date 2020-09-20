def solution(n, connections):
    # ----------------------------------------------------------------------------------------------
    def ToAdjlist(edges):
        """
            Edges are a list list, it assume that the graph undirected 
            returns the adjacency list of the graph. 
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
                This will be the root of the DFSTree. 
        """
        # Phase1: Constructing DFS tree and Level Map ----------------------------------------------
        AdjListDFS = {}  # The Ddj list for the DFS tree. 
        Stack = [startingVertex]
        Visited = set(); Visited.add(startingVertex)
        LevelMap = {}; LevelMap[startingVertex] = 0
        while len(Stack) != 0:
            U = Stack.pop()
            for V in adjList[U]:
                if V not in Visited:
                    NeighboursList = AdjListDFS.get(U, [])
                    NeighboursList.append(V)
                    AdjListDFS[U] = NeighboursList
                    Visited.add(V)
                    Stack.append(V)
                    LevelMap[V] = LevelMap[U] + 1
        
        # Phase 2: Finding the Bridges via Min Pointback--------------------------------------------
        MinPointBack = {}
        Stack = [startingVertex]
        while len(Stack) != 0:
            U = Stack[-1]
            # U is the leaf vertex ----------------------------------------------------------------
            if U not in AdjListDFS:
                MinPointBack = float("+inf")
                for V in [V for V in AdjList[U] if V != U]:
                    MinPointBack = min(MinPointBack, LevelMap[V])
            # U is not the leaf, it will need to recur a bit. --------------------------------------
            else:
                for V in AdjListDFS[U]:
                    Stack.append(V)
            # Merge in the result for getting the bridges in the graph. 
                

                
                    
            
        
        return AdjListDFS


    pass


def main():
    pass

if __name__ == "__main__":
    main()