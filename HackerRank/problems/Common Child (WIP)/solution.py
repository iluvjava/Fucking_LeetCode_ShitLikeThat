def solution(s1, s2):
    T = {}
    def T2(I, J):
        if I < 0 or J < 0: 
            return 0
        return T[I, J]
    for I in range(len(s1)):
        for J in range(len(s2)):
            if I >= 2:
                del T[I - 2, J]
            if s1[I] == s2[J]:
                T[I, J] = T2(I - 1, J - 1) + 1
            else:
                T[I, J] = max(T2(I - 1, J), T2(I, J - 1))
    return T[len(s1) - 1, len(s2) - 1]


def solution_better(s1, s2):
    pass


def main():
    print(solution_better("HARRY", "SALLY"))
    print(solution_better("SHINCHAN", "NOHARAAA"))
    print(solution_better("ABCDEF", "FBDAMN"))
    pass

if __name__ == "__main__":
    main()