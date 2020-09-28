def solution(arr, limit):
    if len(arr) == 1:
        return 1 if arr[0] <= limit else 0

    # Construction of the min-max 2d storage
    Min = [[None]*len(arr) for _ in range(len(arr))]
    Max = [[None]*len(arr) for _ in range(len(arr))]
    
    for I in range(len(arr)):
        Min[I][I] = Max[I][I] = arr[I]
    MaxLen = float("-inf")
    for I in range(len(arr)):
        for J in range(I + 1, len(arr)):
            Min[I][J] = min(Min[I][J - 1], arr[J])
            Max[I][J] = max(Max[I][J - 1], arr[J])
            if Max[I][J] - Min[I][J] <= limit:
                MaxLen = max(MaxLen, J - I + 1)
    
    for R in Min:
        print(R)
    print()
    for R in Max:
        print(R)
    return MaxLen


def main():
    print(solution([4,2,2,2,4,4,2,2], 0))


if __name__ == "__main__":
    main()