def solution_stack(height):

    return

def solution_dp(height):
    # Construct Left Max ---------------------------------------------------------------------------
    MaxHeightLeft = [height[0]]
    for I in range(1, len(height)):
        MaxHeightLeft.append(max(MaxHeightLeft[-1], height[I]))
    # Construct Right Max --------------------------------------------------------------------------
    MaxHeightRight = [height[-1]]
    for I in range(len(height) - 2, -1, -1):
        MaxHeightRight.insert(0, max(height[I], MaxHeightRight[0]))
    # Construct The Optimal Solution ---------------------------------------------------------------
    print("This is the left right max height map: ")
    print(MaxHeightLeft)
    print(MaxHeightRight)
    print("And this is the input array: ")
    print(height)
    Ans = 0
    for I in range(1, len(height) - 1):
        LevelHeight = min(MaxHeightLeft[I - 1], MaxHeightRight[I + 1])
        if height[I] < LevelHeight:
            Ans += LevelHeight - height[I]
    return Ans

def main():
    print(solution_dp([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # print(solution([3, 3, 2, 1, 4]))
    # print(solution([[4, 2, 4, 2, 4, 1, 4]]))
    # print(solution([4, 4, 1, 2, 3, 4, 3, 4, 4, 5]))
    print(solution_dp([1, 2, 3, 4, 5, 6]))
    pass


if __name__ == "__main__":
    main()