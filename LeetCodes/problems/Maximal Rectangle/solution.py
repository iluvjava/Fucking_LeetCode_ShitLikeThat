def solution(arr):
    if len(arr) == 0:
        return 0
    # special case -------------------------------------------------------------
    def SolveLowerDimension(arr):
        T = {}
        T[-1] = 0
        Maximal = 0
        for I in range(len(arr)):
            if arr[I] == 1:
                T[I] = T[I - 1] + 1
                Maximal = max(Maximal, T[I])
            else:
                T[I] = 0
        return Maximal
    
    if len(arr) == 1 or len(arr[0]) == 1:
        if len(arr) == 1:
            return SolveLowerDimension(arr[0])
        return SolveLowerDimension([arr[I][0] for I in range(len(arr))])
       
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
    
    RunningMax = 0
    for I in range(M): 
        for J in range(N):
            if arr[I][J] == 1:
                T1[I, J] = DP1(I - 1, J) + 1
                T2[I, J] = DP2(I, J - 1) + 1
                if DP3(I - 1, J - 1) != (0, 0):
                    T3[I, J] = (
                        min(DP3(I - 1, J - 1)[0], DP1(I - 1, J)) + 1,\
                        min(DP3(I - 1, J - 1)[1], DP2(I, J - 1)) + 1
                        )
                else:
                    if DP1(I - 1, J) > DP2(I, J - 1):
                        T3[I, J] = (DP1(I - 1, J) + 1, 1)
                    else:
                        T3[I, J] = (1, DP2(I, J - 1) + 1)
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
    # --------------------------------------------------------------------------
    return RunningMax


def main():
    arr = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]
    arr = [[int(arr[I][J]) for J in range(len(arr[0]))] for I in range(len(arr))]
    print(f"and the solution is: {solution(arr)}")

    print(solution([[1, 1, 1]]))
    print(solution([[0, 1], [0, 1]]))
    print(solution([[1]*4 for _ in range(3)]))
    pass


if __name__ == "__main__":
    main()