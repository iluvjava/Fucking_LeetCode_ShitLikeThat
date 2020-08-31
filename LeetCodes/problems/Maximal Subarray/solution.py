def solution(nums):
    T = {}
    T[0] = nums[0]
    for I in range(1, len(nums)):
        T[I] = max(T[I - 1] + nums[I], nums[I])
    return max(I for I in T.values())


def main():
    print(solution([-2,1,-3,4,-1,2,1,-5,4]))
    pass


if __name__ == "__main__":
    main()