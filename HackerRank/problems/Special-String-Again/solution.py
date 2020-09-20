def solution_recur_mem(s):
    T = {}
    N = len(s)
    
    def IsSpecial(I, J):
        if I == J or J < I:
            return True
        if J - I == 2:
            T[I, J] = s[I] == s[J]
            return T[I, J]
        if (I, J) in T:
            return T[I, J]
        T[I, J] = IsSpecial(I + 1, J - 1) and s[I + 1] == s[I] and s[J - 1] == s[J]
        return T[I, J]
    
    Counter = 0
    for I in range(N):
        for J in range(I, N):
            Counter += int(IsSpecial(I, J))
    print([s[K: V + 1] for K, V in T.keys() if T[K, V]])
    return Counter


def solution_brute_force(s):
    Counter = 0; N = len(s)
    for I in range(N):
        for J in range(I, N):
            SpecialChar = None
            if s[I] == s[J]:
                SpecialChar = s[I]
            else:
                continue
            IsSpecial = True
            while J - I >= -1:
                if (SpecialChar != s[I] or SpecialChar != s[J]) and I != J:
                    IsSpecial = False
                J -= 1; I += 1
            Counter += int(IsSpecial)
    return Counter


def solution(s):
    T = {}
    N = len(s)
    def IsSpecial(I, J):
        if (I, J) in T:
            return T[I, J]
        Stack = [(I, J)]
        while len(Stack) != 0:
            I, J = Stack[-1]
            if I == J or J < I:
                T[I, J] = True
                Stack.pop()
                continue
            if J - I == 2:
                T[I, J] = s[I] == s[J]
                Stack.pop()
                continue
            if (I + 1, J - 1) not in T:
                Stack.append((I + 1, J - 1))
                continue
            T[I, J] = T[I + 1, J - 1] and s[I + 1] == s[I] and s[J - 1] == s[J]
            Stack.pop()
        return T[I, J]
    Counter = 0
    for I in range(N):
        for J in range(I, N):
            Counter += int(IsSpecial(I, J))
    return Counter

def solution_correct(s):
    N = len(s)
    def StringCollapse():
        Stack = [(s[0], 1)]
        for I in range(1, len(s)):
            if s[I] == Stack[-1][0]:
                Stack[-1] = (Stack[-1][0], Stack[-1][1] + 1)
            else:
                Stack.append((s[I], 1))
        return Stack
    Collapsed = StringCollapse()

    TotalSpecial = 0
    # First Pass Type I
    for C, F in Collapsed:
        TotalSpecial += F*(F + 1)//2
    
    # Second Pass Type II
    for I in range(1, len(Collapsed) - 1):
        A = Collapsed[I - 1]
        B = Collapsed[I]
        C = Collapsed[I + 1]
        if A[0] == C[0] and B[1] == 1:
            K = min(A[1], C[1])
            TotalSpecial += K
    return TotalSpecial


def main():
    print(solution_correct("mnonopoo"))
    print(solution_correct("asasd"))
    print(solution_correct("abcbaba"))
    print(solution_correct("aba"))

    def Hidden():
        with open("hidden_testcase2.txt") as f:
            Lines = f.readlines()
            Expected = Lines[0]
            Inputs = Lines[1]
            print(f"Expected: {Expected}")
            print(f"Actually got: {solution_correct(Inputs)}")
    Hidden()


if __name__ == "__main__":
    main()