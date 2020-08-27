def solution_simple_recur_mem(arr):
    T = {}
    def min_candy_for(i):
        if i >= len(arr) or i < 0:
            return 0
        if i in T:
            return T[i]
        ScoreLeft = 0 if i - 1 < 0 else arr[i - 1]
        ScoreRight = 0 if i + 1 >= len(arr) else arr[i + 1]
        LowerBoundLeft = min_candy_for(i - 1) + 1 if arr[i] > ScoreLeft \
            else 1
        LowerBoundRight = min_candy_for(i + 1) + 1 if arr[i] > ScoreRight\
            else 1
        T[i] = max(LowerBoundLeft, LowerBoundRight)
        return T[i]

    Candies = []
    for I in range(len(arr)):
        Candies.append(min_candy_for(I))
    
    return sum(Candies)


def solution_simplerecur_mem_sackified(arr):
    T = {}  # Recrusion table, storing the result. 
    T[-1] = T[len(arr)] = 0  # Recursion Base Case. 

    def MinCandyFor(i):
        if i in T:
            return T[i]
        RecurStack = [i] # Root. 
        while len(RecurStack) != 0:
            i = RecurStack[-1]
            ScoreLeft = 0 if i - 1 < 0 else arr[i - 1]
            ScoreRight = 0 if i + 1 >= len(arr) else arr[i + 1]
            # Branch Out -------------------------------------------------------
            if arr[i] > ScoreLeft and (i - 1) not in T:
                RecurStack.append(i - 1)
                continue
            if arr[i] > ScoreRight and (i + 1) not in T:
                RecurStack.append(i + 1)
                continue
            # Merge in ---------------------------------------------------------
            LowerBoundLeft = (T[i - 1] + 1) if arr[i] > ScoreLeft else 1
            LowerRightBound = (T[i + 1] + 1) if arr[i] > ScoreRight else 1
            T[i] = max(LowerBoundLeft, LowerRightBound)
            RecurStack.pop() # Only pop when it's solved! 
        return T[i]
    
    Candies = []
    for I in range(len(arr)):
        Candies.append(MinCandyFor(I))

    return sum(Candies)



def main(): 
    print(solution_simplerecur_mem_sackified([4, 6, 4, 5, 6, 2]))
    
    def FailedTestCase():
        arr = [I for I in range(1, 100000 + 1)]
        print(solution_simplerecur_mem_sackified(arr))
    

   


if __name__ == "__main__": 
    main()