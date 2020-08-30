def solution(arr):
    T1, T2, T3 = {}, {}, {}
    # T1: single column continuous max sum
    # T2: single row continuos max sum
    # T3: size of the bottom right continuous rectangle
    M, N = len(arr), len(arr[0])
    def DP1(I, J):
        if I < 0 or J < 0:
            return 0
        return T1[I, J]

    def DP2(I, J):
        if J < 0 or I < 0:
            return 0
        return T2[I, J]

    def DP3(I, J):
        if I < 0 or J < 0:
            return (0, 0)
        return T3[I, J]
    
    RunningMax = float("-inf")
    for I in range(M): 
        for J in range(N):
            if arr[I][J] == 1:
                T1[I, J] = DP1(I - 1, J) + 1
                T2[I, J] = DP2(I, J - 1) + 1
                T3[I, J] = (min(DP3(I - 1, J - 1)[0], DP1(I - 1, J)) + 1,\
                    min(DP3(I - 1, J - 1)[1], DP2(I, J - 1) + 1))
                RunningMax = max(RunningMax, T3[I, J][0]*T3[I, J][1])
            else:
                T1[I, J] = T2[I, J] = 0 
                T3[I, J] = (0, 0)
    # --------------------------------------------------------------------------
    # print out for debugging
    # --------------------------------------------------------------------------
    for R in [[T1[I, J] for J in range(N)] for I in range(M)]:
        print(R)
    print()
    for R in [[T2[I, J] for J in range(N)] for I in range(M)]:
        print(R)
    print()
    for R in [[T3[I, J] for J in range(N)] for I in range(M)]:
        print(R)
    return RunningMax


def main():
    arr = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","1","1","1"]
    ]
    arr = [[int(arr[I][J]) for J in range(len(arr[0]))] for I in range(len(arr))]
    solution(arr)
    pass


if __name__ == "__main__":
    main()