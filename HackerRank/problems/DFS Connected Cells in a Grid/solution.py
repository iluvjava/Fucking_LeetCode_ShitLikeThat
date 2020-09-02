def solution(grid):
    M, N = len(grid), len(grid[0])
    def Grid(I, J):
        if (I < 0 or J < 0) or (I >= len(grid) or J >= len(grid[0])):
            return 0
        return grid[I][J]
    
    Visited = set()
    def DFS(i, j):
        Stack = [(i, j)]  # assume i, j is filled
        SizeCC = 0
        Visited.add((i, j))
        while len(Stack) != 0:
            I, J = Stack.pop()
            SizeCC += 1
            for K, W in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if (Grid(I + K, J + W) == 1) and ((I + K, J + W) not in Visited):
                    Stack.append((I + K, J + W))
                    Visited.add((I + K, J + W))
        return SizeCC
    
    MaxComponentSize = 0
    for I in range(M): 
        for J in range(N):
            if Grid(I, J) == 1 and (I, J) not in Visited:
                MaxComponentSize = max(DFS(I, J), MaxComponentSize)
    return MaxComponentSize

def main():
    TestArr1 = [[1, 1,  0,  0],
                [0, 1,  1,  0],
                [0, 0,  1,  0], 
                [1, 0,  0,  0]]
    print(solution(TestArr1))
    

if __name__ == "__main__":
    main()