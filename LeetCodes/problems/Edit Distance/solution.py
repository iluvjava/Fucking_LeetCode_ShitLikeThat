def solution_dp_tabularized(w1, w2):
    if w1 == w2:
        return 0
    M, N = len(w1), len(w2)
    if M == 0 or N == 0:
        return max(M, N)
    T = {}
    
    def DP(I, J):
        if I < 0 and J < 0:
            return 0
        if I < 0 or J < 0:
            return max(I, J) + 1
        if (I, J) in T:
            return T[I, J]
        raise RuntimeError("Tabular Leakage.")
    
    
    for I in range(M):
        for J in range(N):
            L1, L2 = w1[I], w2[J]
            MisMatch = int(L1 != L2)
            Edit = min(DP(I - 1, J), DP(I, J - 1)) + 1
            if MisMatch:
                Replace = DP(I - 1, J - 1) + 1
                T[I, J] = min(Replace, Edit)
            else:
                NoReplace = DP(I - 1, J - 1)
                T[I, J] = NoReplace
    for R in [[T[I, J] for I in range(M)] for J in range(N)]:
        print(R)
    return T[M - 1, N - 1]


def solution_recur_mem(w1, w2):
    M, N = len(w1), len(w2)
    T = {}
    def recur(I, J):
        if (I, J) in T:
            return T[I, J]
        if I < 0 or J < 0:
            return max(I, J) + 1
        L1, L2 = w1[I], w2[J]
        if L1 == L2:
            return recur(I - 1, J - 1)  # it won't change the edit distance!
        T[I, J] = 1 + min(recur(I - 1, J), recur(I, J - 1), recur(I - 1, J - 1))
        return T[I, J]

    return recur(M - 1, N - 1)
        
    

def main():
    print(solution_dp_tabularized("horse", "ros"))
    word1, word2= "intention", "execution"
    print(solution_dp_tabularized(word1, word2))
    pass

if __name__ == "__main__":
    main()