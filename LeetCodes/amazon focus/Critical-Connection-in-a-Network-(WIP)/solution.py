



# def solution(n, connections):
#     # Construct the adjacency list for the graph by the edges
#     def GetAdjlist():
#         Adjlist = {}
#         for L in connections:
#             [U, V] = L
#             NeiU = Adjlist.get(U, [])
#             NeiV = Adjlist.get(V, [])
#             NeiU.append(V);NeiV.append(U)
#             Adjlist[U] = NeiU
#             Adjlist[V] = NeiV
#         return Adjlist

#     GraphAdjlist = GetAdjlist()
#     print("The adjlist of the graph has been constructed: ")
#     print(GraphAdjlist)
#     # Get the DFS tree out of the adjacency list of the graph.
#     # Also contruct the level map of the tree while doing this
#     # Tree adjlist is gonna be directed and it will be a tree. 
#     def DfsTree(adjList, startingVertex):
#         Visited = set([startingVertex]); 
#         Stack = [startingVertex]
#         TreeAdjList = {}
#         LevelMap = {}; LevelMap[startingVertex] = 0
#         while Stack:
#             V = Stack.pop()
#             for Nv in adjList[V]:
#                 if Nv not in Visited:
#                     Visited.add(Nv)
#                     Stack.append(Nv)
#                     LevelMap[Nv] = LevelMap[V] + 1
#                     TreeNeighbours = TreeAdjList.get(V, [])
#                     TreeNeighbours.append(Nv)
#                     TreeAdjList[V] = TreeNeighbours
#         return TreeAdjList, LevelMap

#     # Keep track of the minimum point back for each of the substree recrursively and then 
#     # remove the critical edges accroding. 

#     TreeAdjlist, LevelMap = DfsTree(GraphAdjlist, 0)
#     print("Adjlist of the dfs tree: ")
#     print(TreeAdjlist)
#     print("Levelmap of the dfs tree")
#     print(LevelMap)

    
#     def GetCriticalEdges(treeRoot = 0, Criticals = None, MinPointback=None):
#         MinPointback = {} if MinPointback is None else MinPointback
#         Criticals = [] if Criticals is None else Criticals
#         if treeRoot not in TreeAdjlist:  # it's a leaf
#             MinPointback[treeRoot] = float("inf")
#             for Nroot in GraphAdjlist[treeRoot]:
#                 if LevelMap[Nroot] > LevelMap[treeRoot] + 1:
#                     MinPointback = min(MinPointback[treeRoot], LevelMap[Nroot])
#             print(f"MinPointback Updated: {MinPointback}")
#             return
#         # Branch out:
#         for Child in TreeAdjlist[treeRoot]:
#             GetCriticalEdges(Child, Criticals, MinPointback)
#         # Merge in: 
#         MinPointback[treeRoot] = float("inf")

#         for Nroot in GraphAdjlist[treeRoot]:
#             if LevelMap[Nroot] > LevelMap[treeRoot] + 1:
#                     MinPointback = min(MinPointback[treeRoot], LevelMap[Nroot])

#         for Child in TreeAdjlist[treeRoot]:
#             MinPointback[treeRoot] = min(MinPointback[treeRoot], MinPointback[Child], LevelMap[Child])
#             if MinPointback[Child] > LevelMap[treeRoot]:
#                 Criticals.append((treeRoot, Child))
#         print(f"Minpointback updated: {MinPointback}")
        
#         return Criticals
        
    """
    def GetCriticalEdges(treeRoot = 0):
        # Root doesn't have min point back
        Criticals = []
        PointBackDict = {}
        Stack = [treeRoot]
        while Stack:
            print(Stack)
            V = Stack[-1]
            if V not in TreeAdjlist:
                MinPointBack = float("+inf")
                for Nv in GraphAdjlist[V]:
                    if LevelMap[Nv] > LevelMap[V] - 1:  # Not its parent
                        MinPointBack = min(LevelMap[Nv], MinPointBack)
                PointBackDict[V] = MinPointBack
                Stack.pop()
                continue
            else:
                Exc = False
                for C in TreeAdjlist[V]:
                    if C not in PointBackDict:
                        Stack.append(C)
                        Exc = True
                if Exc:
                    continue
                MinPointPackAllChildren = float("inf")
                for C in TreeAdjlist[V]:
                    MinPointPackAllChildren = min(MinPointPackAllChildren, PointBackDict[C])
                    if PointBackDict[C] < LevelMap[V]:
                        Criticals.append((V, C))
                Stack.pop()
        print(f"Criticals: {Criticals}")
        print(f"MinPointBackDict: {PointBackDict}")
        return Criticals
        """

    # CriticalEdges = GetCriticalEdges()
    # print(f"Critical Eges: {CriticalEdges}")
    


def solution_bruteforce(n, connections):

    def ToAdjlist(edges):
        pass

    def BFSsize(startingVertex, Adjlist):
        pass

    for L in connections:

        pass

    pass

# def solution(n, connections):
#     # ----------------------------------------------------------------------------------------------
#     def ToAdjlist(edges):
#         """
#             Edges are a list list, it assume that the graph undirected 
#             returns the adjacency list of the graph. 
#         """
#         AdjList = {}
#         for L in edges: 
#             [U, V] = L
#             UNeighbours = AdjList.get(U, [])
#             VNeighbours = AdjList.get(V, [])
#             UNeighbours.append(V)
#             VNeighbours.append(U)
#             AdjList[U] = UNeighbours
#             AdjList[V] = VNeighbours
#         print(f"Adjlist: {AdjList}")
#         return AdjList
    
#     AdjList = ToAdjlist(connections)

#     def GetDFSTree(adjList, startingVertex):
#         """
#                 Given a Adjacency list this function will return another adjlist that represents
#                 the DFS tree of the given graph. 
#             :para startingVertex: 
#                 This will be the root of the DFSTree. 
#         """
#         # Phase1: Constructing DFS tree and Level Map ----------------------------------------------
#         AdjListDFS = {}  # The Ddj list for the DFS tree. 
#         Stack = [startingVertex]
#         Visited = set(); Visited.add(startingVertex)
#         LevelMap = {}; LevelMap[startingVertex] = 0
#         while len(Stack) != 0:
#             U = Stack.pop()
#             for V in adjList[U]:
#                 if V not in Visited:
#                     NeighboursList = AdjListDFS.get(U, [])
#                     NeighboursList.append(V)
#                     AdjListDFS[U] = NeighboursList
#                     Visited.add(V)
#                     Stack.append(V)
#                     LevelMap[V] = LevelMap[U] + 1
        
#         # Phase 2: Finding the Bridges via Min Pointback--------------------------------------------
#         MinPointBack = {}
#         Stack = [startingVertex]
#         EdgesToRemove = []
#         while len(Stack) != 0:
#             U = Stack[-1]
#             # U is the leaf vertex ----------------------------------------------------------------
#             if U not in AdjListDFS:
#                 MinPointBack = float("+inf")
#                 for V in [V for V in AdjList[U] if V != U]:
#                     MinPointBack = min(MinPointBack, LevelMap[V])
#             # U is not the leaf, it will need to recur a bit. --------------------------------------
#             else:
#                 for V in AdjListDFS[U]:
#                     Stack.append(V)
#             # Merge in the result for getting the bridges in the graph. 
            
#         return AdjListDFS


    


def main():
    def Test1():  # A full graph of size 4, containing all the edges 
        n = 4
        Arr = [
            [0, 3], [0, 1], [0, 2],
            [2, 3], [1, 2], [1, 3], [2, 4]
        ]
        solution(n, Arr)

    
    Test1()

if __name__ == "__main__":
    main()