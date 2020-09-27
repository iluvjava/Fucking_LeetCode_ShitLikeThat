def solution(arr):
    for I in range(len(arr)):
        for J in range(len(arr) - 1, I, -1):
            if str(arr[J]) + str(arr[I]) > str(arr[I]) + str(arr[J]):
                arr[I], arr[J] = arr[J], arr[I]
        print(arr)
    return "".join(map(str, arr))


def main():
    def Test1():
        Arr = [998, 99, 997, 999]
        print(solution(Arr))
    Test1()


if __name__ == "__main__":
    main()