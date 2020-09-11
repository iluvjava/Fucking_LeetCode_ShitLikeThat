def solution_failed(roads, machines):
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


class UnionFind:
    """
        Gonna appreciate simplicity
    """
    def __init__(self):
        self._M = {}
        pass

    def __call__(self, element):
        """
            get the representative of the element.

            * If the element is never added, then it will be added
            to the data structure and it will return itself.

            * Path compression
        :return:
            Representative or itself in the case that the element
            never really appeared in the data-structure before.
        """
        if element not in self._M:
            self._M[element] = None  # Root.
            return element

        if self._M[element] is None:
            return element
        Representative = self(self._M[element])
        self._M[element] = Representative
        return Representative

    def join(self, a, b):
        Represent1 = self(a)
        Represent2 = self(b)
        if Represent1 == Represent2:
            return
        self._M[Represent1] = Represent2


class UnionSetJoin(UnionFind):
    """
        The representative of the joined sets are now literally a
        set with all the elements that got joined together.
    """

    def __init__(self):
        super().__init__()
        self._ElementToInts = {}
        self._Sets = []

    def __call__(self, element):
        if element not in self._ElementToInts:
            self._ElementToInts[element] = len(self._Sets)
            self._Sets.append(set([element]))
            return super().__call__(element)
        return super().__call__(element)

    def join(self, a, b):
        if self(a) == self(b):
            return
        SetReprOfB = self._Sets[self._ElementToInts[self(b)]]
        SetReprOfB |= self._Sets[self._ElementToInts[self(a)]]
        super().join(a, b)

    def get_joined_set(self, element):
        return self._Sets[self._ElementToInts[self(element)]]

    def __repr__(self):
        s = ""
        for K in self._ElementToInts:
            s += f"{K}: {self.get_joined_set(K)}\n"
        return s


def solution(roads, machines):
    roads = map(tuple, roads); machines = set(machines)
    roads = sorted(roads, key=lambda x: x[2], reverse = True)
    Uf = UnionFind()
    TotalEdgeCost = 0
    for U, V, W in roads:
        if not (Uf(U) in machines and Uf(V) in machines):
            if Uf(U) in machines:
                Uf.join(V, U)
            else:
                Uf.join(U, V)
        else:
            # Can't join edges skip 
            TotalEdgeCost += W
    return TotalEdgeCost


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