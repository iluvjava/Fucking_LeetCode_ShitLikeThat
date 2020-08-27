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
    
    


def main():

    pass


if __name__ == "__main__":
    main()