def countInversions(arr):    
    return countInversions_recur([arr, [0]*len(arr)], 0, len(arr))


def countInversions_recur(twoArrs, start, end):
    """

        Range under examination: start <= I < end. 

        :param refArr: 
            A temp storage for the arr when merging.
        :param refArr: 
            
    """
    arr, refArr = twoArrs[0], twoArrs[1]
    if end - start <= 2: # Base Case -----------------------------------------------------------------------------------
        if end - start == 1:
            return 0
        else:
            Inversions = 1 if arr[start] > arr[end - 1] else 0
            if Inversions != 0:
                arr[start], arr[end - 1] = arr[end - 1], arr[start]
            return Inversions
    
    # Recur ------------------------------------------------------------------------------------------------------------
    M = (start + end)//2 + 1 
    LeftInversion, RightInversion = \
         countInversions_recur(twoArrs, start, M), countInversions_recur(twoArrs, M, end)
    MergeInversion = 0
    
    # Merge ------------------------------------------------------------------------------------------------------------
    I, J, K = start, M, 0  # Running indices in left, right, and the offset
    # start <= I < M, M <= J < end
    
    while I < M and J < end:
        refArr[start + K] = min(arr[I], arr[J])
        if arr[I] <= arr[J]:
            I += 1
        else:
            MergeInversion += M - I
            J += 1
        K += 1
    
    if I < M:
        refArr[start + K: end] = arr[I:M]
    
    if J < end: 
        refArr[start + K: end] = arr[J:end]
    
    arr[start:end] = refArr[start:end]
    # Return -----------------------------------------------------------------------------------------------------------
    return LeftInversion + RightInversion + MergeInversion


def brute_force_inversion_count(arr):
    counter = 0
    for I in range(len(arr)):
        for J in range(I + 1, len(arr)):
            if arr[I] > arr[J]:
                counter += 1
    return counter


def main():

    def Test1():
        Arr1 = [1, 2, 3]
        Arr2 = [3, 2, 1]
        print(brute_force_inversion_count(Arr1))
        print(brute_force_inversion_count(Arr2))
        print(countInversions(Arr1))
        print(countInversions(Arr2))
        print(countInversions(list(reversed([I for I in range(21)]))))
    
    def Test2():
        from random import shuffle, random
        ArraySize = 10
        Range = 5
        for _ in range (1000):
            arr = [int(random()*Range) for I in range(ArraySize)]
            shuffle(arr)
            Res1, Res2 =  brute_force_inversion_count(arr.copy()), countInversions(arr.copy())
            print(f"arr: {arr}")
            print(f"arr: {Res1 == Res2}")
            assert Res1 == Res2, f"{Res1} != {Res2}"

    def Test3():
        with open("hidden_testcase7.txt") as f:
            lines = f.readlines()
            Arrs = [list(map(int, lines[I].split())) for I in[2, 4, 6, 8, 10]]
            Expected = [int(lines[I]) for I in [11, 12, 13, 14, 15]]
            for I, Arr in enumerate(Arrs):
                print(f"Expected: {Expected[I]}")
                print(f"Actually got: {countInversions(Arr)}")

    Test2()
    Test1()
    Test3()


if __name__ == "__main__":
    main()