
def solution(arr):
    T = [float("-inf") for _ in range(len(arr) + 1)]
    T[0] = arr[0]
    T[1] = max(arr[0], arr[1])
    for I in range(2, len(arr)):
        T[I] = max(arr[I] + max(T[I - 2], 0), T[I - 1])
    return T[len(arr) - 1]


def main():
    print(solution([-2, 1, 3, -4, 5]))
    pass


if __name__ == "__main__":
    main()