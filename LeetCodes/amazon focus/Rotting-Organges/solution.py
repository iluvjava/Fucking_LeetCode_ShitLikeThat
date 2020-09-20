def solution(arr):
    Depth = [[0]*len(arr[0]) for _ in range(len(arr))]
    def WrapArr(i, j):
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            return 0
        return arr[i][j]
    def MarkRotten(i, j):
        arr[i][j] = 2
    def BFS (theQueue):
        """
            DFS is going to count the deepest depth it can go starting with 
            this Vertex. 
        """
        # I, J already rotten.
        Neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while theQueue:
            I, J = theQueue.pop(0)
            for K, W in Neighbours:
                U, V = I + K, J + W
                if WrapArr(U, V) == 1:
                    theQueue.append((U, V))
                    MarkRotten(U, V)
                    Depth[U][V] = Depth[I][J] + 1
    Rotten = []
    for I, J in [(I, J) for I in range(len(arr)) for J in range(len(arr[0]))]:
        if WrapArr(I, J) == 2:
           Rotten.append((I, J))
    BFS(Rotten)
    AllRotten = False
    for I, J in [(I, J) for I in range(len(arr)) for J in range(len(arr[0]))]:
        if WrapArr(I, J) == 1:
            return -1
    return max(max(A for A in Depth[I]) for I in range(len(Depth)))


def main():
    def TestCase1():
        Arr = \
        [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
        print(solution(Arr))

    def TestCase2():
        Arr = \
        [
           [1, 2],
           [2, 1]
        ]
        print(solution(Arr))
    TestCase1()
    TestCase2()


if __name__ == "__main__":
    main()