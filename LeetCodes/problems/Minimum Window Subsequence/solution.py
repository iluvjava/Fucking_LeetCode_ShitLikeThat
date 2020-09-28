def solution(s, subSequence):
    T = {}
    T[0, 0] = 0 if subSequence[0] == s[0] else float("inf")
    for I in range(1, len(s)):
        if s[I] == subSequence[0]:
            T[I, 0] = 0 
        else:
            T[I, 0] = T[I - 1, 0] + 1
    
    for J in range(1, len(subSequence)):
        T[0, J] = float("+inf")

    for I in range(1, len(s)):
        for J in range(1, len(subSequence)):
            if s[I] == subSequence[J]:
                T[I, J] = T[I - 1, J - 1] + 1
            else:
                T[I, J] = T[I - 1, J] + 1

    # PrintOut = \
    # [[T[I, J] for I in range(len(s))] for J in range(len(subSequence))]
    # for R in PrintOut: 
    #     print(R)

    MinPointBackIndex = None
    MinPointBack = float("inf")
    for I in range(len(s)):
        if T[I, len(subSequence) - 1] < MinPointBack:
            MinPointBack = T[I, len(subSequence) - 1]
            MinPointBackIndex = I
    
    if MinPointBack == float("inf"):
        return ""    

    return s[MinPointBackIndex - MinPointBack :MinPointBackIndex + 1]





def main():
    Soln = solution("abcdfe", "abcde")
    print(Soln)
    Soln = solution("abcdebdde", "bde")
    print(Soln)
    Soln = solution("-ab--c-", "abc")
    print(Soln)
    Soln = solution("-aaa-b-ccc-", "abc")
    print(Soln)



if __name__ == "__main__":
    main()