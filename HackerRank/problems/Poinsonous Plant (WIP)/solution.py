def solution(arr):
    RunningMax = 0
    Stack = []
    for I in reversed(arr):
        Counter = 0
        while (len(Stack) != 0) and (I < Stack[-1]):
            Counter += 1
            Stack.pop()
            RunningMax = max(RunningMax, Counter)
        Stack.append(I)
    return RunningMax


def main():
    print(solution([4, 3, 2, 1]))
    print(solution([1, 2, 3, 4]))
    print(solution([6, 5, 8, 4, 7, 10, 9]))


if __name__ == "__main__":
    
    main()