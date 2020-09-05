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

def solution_brute(arr):
    SomePlantDied = True
    Days = 0
    print(f"Day 0: {arr}")
    while SomePlantDied:
        Filter = [False]*len(arr)  # To remove
        SomePlantDied = False
        for I in range(1, len(arr)):
            if arr[I] > arr[I - 1]:
                Filter[I] = True
                SomePlantDied = True
        if not SomePlantDied:
            break
        else:
            print(f"Day {Days}: {arr}")
            Days += 1
        arr = [arr[I] for I in range(len(arr)) if not Filter[I]]
    return Days

def main():
    print(solution([4, 3, 2, 1]))
    print(solution_brute([4, 3, 2, 1]))
    print(solution([1, 2, 3, 4]))
    print(solution_brute([1, 2, 3, 4]))
    print(solution([6, 5, 8, 4, 7, 10, 9]))
    print(solution_brute([6, 5, 8, 4, 7, 10, 9]))

    def Hidden_Testcase():
        with open("hidden_testcase_23.txt") as f:
            [Line1, Line2] = f.readlines()
            Line1 = list(map(str, Line1.split()))
            Line2 = str(Line2)
            print(f"Expected: {Line2}")
            print(f"Actually got: {solution(Line1)}")

    def TestForCounterExample():
        from random import shuffle, random
        Array = [int(random()*10) for _ in range(5)]
        for _ in range(10000):
            shuffle(Array)
            Soln1, Soln2 = solution(Array), solution_brute(Array)
            assert Soln1 == Soln2, f"Failed, input:{Array}, soln1: {Soln1}, soln2: {Soln2}"
        
    
    Hidden_Testcase()
    TestForCounterExample()

if __name__ == "__main__":
    
    main()