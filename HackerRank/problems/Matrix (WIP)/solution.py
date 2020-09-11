def solution(roads, machines):
    EdgesWeight, AdjList = {}, {}
    for U, V, Weight in roads:
        EdgesWeight[U, V] = EdgesWeight[V, U] = Weight
        AdjList[U] = AdjList.get(U, []) + [V]
        AdjList[V] = AdjList.get(V, []) + [U]
    
    MinimumCosts = 0
    TheSearchPath = []  # for recursion

    def DFSTreeSearch(Root):
        nonlocal MinimumCosts
        TheSearchPath.append(Root)
        print(TheSearchPath)
        # Record Mincost from Path  --------------------------------------------
        if Root in machines and len(TheSearchPath) >= 2:
            Cost = float("+inf")
            for I in range(len(TheSearchPath) - 1, 0, -1):
                Cost = min(
                    Cost, 
                    EdgesWeight[TheSearchPath[I], TheSearchPath[I - 1]]
                    )
                if (TheSearchPath[I - 1] in machines):
                    break  # Found another machine on the path
            MinimumCosts += Cost
        
        for Child in AdjList[Root]:
            if Child not in TheSearchPath:
                DFSTreeSearch(Child)

        TheSearchPath.pop()
        return # No forloop or forloop is out. 
        
    DFSTreeSearch(machines[0])
    return MinimumCosts

        
if __name__ == "__main__":
    def main():
        def Test1():
            roads = [[2, 1, 8],
                    [1, 0, 5],
                    [2, 4, 5], 
                    [1, 3, 4]]
            machines = [2, 4, 0]
            soln = solution(roads, machines)
            print(f"The solution is: {soln}")
        
        def Test2():
            roads = [
                [0, 3, 3], 
                [1, 4, 4],
                [1, 3, 4],
                [0, 2, 5]
            ]
            machines = [1, 3, 4]
            soln = solution(roads, machines)
            print(f"The solution is: {soln}")
        Test1(); Test2()
       
    main()