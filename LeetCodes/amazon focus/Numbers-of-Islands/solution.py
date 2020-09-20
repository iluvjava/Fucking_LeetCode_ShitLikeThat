def solution(arr):
    arr = [[int(arr[I][J])for J in range(len(arr[0]))] for I in range(len(arr))]
    def ArrWrapped(i, j):
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            return 0
        return arr[i][j]
    def MarkVisited(i, j):
        if i < 0 or j < 0 or i >= len(arr) or j > len(arr[0]):
            return 
        arr[i][j] = 0
    def StartBFS(i, j):
        Neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        Stack = [(i, j)]
        while len(Stack) != 0:
            I, J = Stack.pop(0)
            for K, W in Neighbours:
                K, W = I + K, J + W
                if ArrWrapped(K, W) != 0:
                    MarkVisited(K, W)
                    Stack.append((K, W))
        return  # Ended
    ConnectedComponents = 0
    for I, J in [(I, J) for I in range(len(arr)) for J in range(len(arr[0]))]:
        if ArrWrapped(I, J) != 0: 
            StartBFS(I, J)
            ConnectedComponents += 1
    return ConnectedComponents    
    


def main():
    def Test1():
        Arr = [
            [1, 0, 0, 0, 0, 0], 
            [0, 1, 1, 0, 1, 1],  
            [0, 1, 1, 0, 1, 1],  
            [0, 0, 1, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0]
        ]
        print(solution(Arr))
    Test1()

if __name__ == "__main__":
    main()