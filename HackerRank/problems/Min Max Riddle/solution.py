def immediate_right_smaller(arr):
    """
        If out side of the range, then it will be filled with value: None
    """
    Indices = [None]*len(arr)  # Indices of immediate smaller on right side.
    Stack = []  # Stores indices of elements in arr, initialized with some dummy value.
    for I, V in enumerate(arr):
        while (len(Stack) != 0) and V < arr[Stack[-1]]:
            Indices[Stack.pop()] = I
        Stack.append(I)
    return Indices


def immediate_left_smaller(arr):
    """
        Just modify it a bit and then use what we already have.
    """
    arr = list(reversed(arr))
    Indices = immediate_right_smaller(arr)
    N = len(Indices)
    # Swap it because we reversed it at the beginning. 
    Indices = [(N - 1 - I) if I is not None else None for I in Indices] 
    return list(reversed(Indices))


def immediate_smaller_bothside(arr):
    """
        Package 2 of the routines of left and right together to find 
        the indices for left/right smaller of an element in the array. 
    """
    Left, Right = immediate_left_smaller(arr), immediate_right_smaller(arr)
    Left = [-1 if I is None else I for I in Left]
    Right = [len(arr) if I is None else I for I in Right]
    return Left, Right


def solution(arr):
    """
        This is the solution to the problem
    """
    Left, Right = immediate_smaller_bothside(arr)
    print(f"left and right: {Left}, {Right}")
    WinSize = [(R - L - 1) for L, R in zip(Left, Right)]
    print(f"Winsize: {WinSize}")
    Ans = [float("-inf")]*len(arr)  # To store the result
    for I, V in enumerate(WinSize):
        Ans[V - 1] = max(Ans[V - 1], arr[I])

    if Ans[len(Ans) - 2] == float("-inf"):
        Ans[len(Ans) - 2] = Ans[len(Ans) - 1]

    for I in reversed(range(len(Ans) - 2)):
        if Ans[I] == float("-inf"):
            Ans[I] = max(Ans[I + 1], Ans[I + 2])
        pass
    return Ans


def main():
    def Test1():
        print(immediate_right_smaller([1, 2, 3, 2]))
        print(immediate_right_smaller([1, 2, 3, 4]))
        print(immediate_right_smaller([4, 3, 2, 1]))
        print(immediate_left_smaller([1, 3, 1, 5, 6, 7, 2]))

    def Test2():
        Array = [1, 2, 3, 5, 1, 13, 3]
        print(solution(Array))
        Array = [3, 5, 4, 7, 6, 2]
        print(solution(Array))
    Test2()
    pass


if __name__ == "__main__":
    main()