def solution(arr, k):
    if k == 1:
        return arr
    # Constructing left/right partial sum for the partitions of the array.
    # --------------------------------------------------------------------------
    Lmax = [float("-inf")]*len(arr)  # delete first element afterwards. 
    Lmax[0] = arr[0]
    for I in range(1, len(arr)):
        if (I + 1)%k == 1:
            Lmax[I] = arr[I]
        else:
            Lmax[I] = max(arr[I], Lmax[I - 1])
    Rmax = [float("-inf")]*len(arr)
    Rmax[-1] = arr[-1]
    for I in range(len(arr) - 2, -1, -1):
        if (I + 1)%k == 0:
            Rmax[I] = arr[I]
        else:
            Rmax[I] = max(arr[I], Rmax[I + 1])
    # Using the recurrence to construct the value of the solution: 
    # --------------------------------------------------------------------------
    Accumulate = []
    for I in range(len(arr) - k + 1):
        Accumulate.append(max(Rmax[I], Lmax[I + k - 1]))

    return Accumulate

"""
Dubug notes: I = 5
Lmax:
[1, 3, 3, -3, |5, 5, 6|, 7]
Rmax:
[3, 3, -1, 5, |5, 3, 7|, 7]


"""


def main():
    def Test1():
        Arr = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        print(solution(Arr, k))
    Test1()



if __name__ == "__main__":
    main()