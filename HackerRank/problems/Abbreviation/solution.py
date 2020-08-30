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


def solution_failed(a, b):
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


def solution(a, b):
    T = {}
    M, N = len(a), len(b)
    for I in range(M):
        for J in range(N):
            # A[I] is upper cased letter 
            if a[I].upper() == a[I]:
                T[I, J] = T.get((I, J - 1), False) or \
                    (T.get((I - 1, J - 1), False) or a[I] == b[J])
            else:  
            # A[I] is a lower cased letter
                T[I, J] = T.get((I - 1, J), False) or \
                    (T.get((I - 1, J - 1), True) and a[I].upper() == b[J])
    
    T = [[("T" if T[I, J] else "F") for I in range(M)] for J in range(N)]
    for R in T:
        print(R)
    return T[J][I]


def solution_recur_mem_failed(a, b):
    T = {}  # Param map to results ---------------------------------------------
    def recurFunc(a, b):
        # Base -----------------------------------------------------------------
        if (a, b) in T:
            return T[a, b]
        
        if len(a) < len(b):
            T[a, b] = False
            return False
        
        if a.upper() == a:
            T[a, b] = a == b
            return T[a, b]
        
        # A contains at least one lower cased letter. --------------------------
        L, I = a[0], 0
        
        while a[I].lower() != a[I]: # Find first lower cased letter ------------
            I += 1
            L = a[I]
        
        if L.lower() == L:  # Is lower -----------------------------------------
            Case1 = recurFunc(a[:I] + a[I + 1:], b)  # remove L ----------------
            a_cap = list(a)
            a_cap[I] = a_cap[I].upper()
            Case2 = recurFunc("".join(a_cap), b)
            T[a, b] = Case1 or Case2
        else:
            raise RuntimeError("WTF")

        return T[a, b]
    
    return recurFunc(a, b)


def solution_recur_mem(a, b):
    T = {}
    def recur(I, J):  # If a[:I + 1], b[:J + 1] is a match. 
        if (I, J) in T:
            return T[I, J]
        if I < 0 and J < 0:
            return True
        if I < 0:
            return False
        if J < 0:
            return True
        
        L1, L2 = a[I], b[J]
        if L1.lower() == L1:  # L1 is lower  
            Case1 = recur(I - 1, J)  # delet L1
            Case2 = recur(I - 1, J - 1) and L1.upper() == L2 # Cap L1
            T[I, J] = Case1 or Case2
        else: # L1 is upper
            Case3 = L1 == L2 and recur(I - 1, J - 1)
            T[I, J] = Case3
        return T[I, J]
    M, N = len(a) - 1, len(b) - 1
    return recur(M, N)


def solution_tablularized(a, b):
    T = {}
    M, N = len(a) - 1, len(b) - 1
    
    def DP(I, J):
        if (I, J) in T:
            return T[I, J]
        if I < 0 and J < 0:
            return True
        if I < 0:
            return False
        if J < 0:
            return True
    for I in range(M):
        for J in range(N):
            L1, L2 = a[I], b[J]
            if L1.lower() == L1:
                T[I, J] = DP(I - 1, J) or (DP(I - 1, J - 1) and L1.upper() == L2)
            else:
                T[I, J] = L1 == L2 and DP(I - 1, J - 1)
    return T[M - 1, N - 1]


def main():

    def Bleh():
        a, b = "AfPAN", "APZNC"
        print(f"Get: {solution(a, b)}, Expects: False")
        a, b = "AbcDE", "ABDE"
        print(f"Get: {solution(a, b)}, Expects: True")
        a, b = "beFgH", "EFG"
        print(f"Get: {solution(a, b)}, Expects: False")
    
    def Test1():
        a, b = "AfPAN", "APZNC"
        print(f"Get: {solution_tablularized(a, b)}, Expects: False")
        a, b = "AbcDE", "ABDE"
        print(f"Get: {solution_tablularized(a, b)}, Expects: True")
        a, b = "beFgH", "EFG"
        print(f"Get: {solution_tablularized(a, b)}, Expects: False")
        a = "RDWPJPAMKGRIWAPBZSYWALDBLDOFLWIQPMPLEMCJXKAENTLVYMSJNRJAQQPWAGVcGOHEWQYZDJRAXZOYDMNZJVUSJGKKKSYNCSFWKVNHOGVYULALKEBUNZHERDDOFCYWBUCJGbvqlddfazmmohcewjg"
        b = "RDPJPAMKGRIWAPBZSYWALDBLOFWIQPMPLEMCJXKAENTLVYMJNRJAQQPWAGVGOHEWQYZDJRAXZOYDMNZJVUSJGKKKSYNCSFWKVNHOGVYULALKEBUNZHERDOFCYWBUCJG"
        print(f"Get: {solution_tablularized(a, b)}, Expects: False")
        a = "MBQEVZPBjcbswirgrmkkfvfvcpiukuxlnxkkenqp"
        b = "MBQEVZP"
        print(f"Get: {solution_tablularized(a, b)}, Expects: False")
        a = "DINVMKSOfsVQByBnCWNKPRFRKMhFRSkNQRBVNTIKNBXRSXdADOSeNDcLWFCERZOLQjEZCEPKXPCYKCVKALNxBADQBFDQUpdqunpelxauyyrwtjpkwoxlrrqbjtxlkvkcajhpqhqeitafcsjxwtttzyhzvh"
        b = "DINVMKSOVQBBCWNKPRFRKMFRSNQRBVNTIKNBXRSXADOSNDLWFCERZOLQEZCEPKXPCYKCVKALNBADQBFDQU"
        print(f"Get: {solution_tablularized(a, b)}, Expects: True")
    Test1()
        

if __name__ == "__main__":
    main()