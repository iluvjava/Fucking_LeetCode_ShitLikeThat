def longest_common_substring(a, b):
    T = {}
    T2 = {}
    T[0, -1] = T[-1, 0] = T[-1, -1] = 0
    # Iterative construct the table ----------------------------------------------------------------
    for I in range(len(a)):
        for J in range(len(a)):
            if a[I] == a[J]:
                T[I, J] = T[I - 1, J - 1] + 1
                T2[I, J] = 1
            else:
                if T[I - 1, J] >= T[I, J - 1]:
                    T[I, J] = T[I - 1, J]
                    T2[I, J] = 2
                else:
                    T[I, J] = T[I, J - 1]
                    T2[I, J] == 3
    # back trace -----------------------------------------------------------------------------------
    return T, T2

def solution(a, b):
    T = {}
    M, N = len(a), len(b)
    S = set()  # Longest Common Subsequence
    for I in range(M):
        for J in range(N):
            L1, L2 = a[I], b[J]
            if L1.upper() == L2:
                S.add(I)
                T[I, J] = T.get((I - 1, J - 1), 0) + 1
            else:
                T[I, J] = max(T.get((I - 1, J), 0), T.get((I, J - 1), 0))
    MustBeLower = all(a[I].lower() == a[I] for I in range(M) if I not in S)
    return T[I, J] == N and MustBeLower


def main():
    a, b = "AfPAN", "APZNC"
    print(f"Get: {solution(a, b)}, Expects: False")
    a, b = "AbcDE", "ABDE"
    print(f"Get: {solution(a, b)}, Expects: True")
    a, b = "beFgH", "EFG"
    print(f"Get: {solution(a, b)}, Expects: False")


if __name__ == "__main__":
    main()