

def solution(arr):
    T1, T2, T3 = {}, {}, {}

    def DP1(I):
        if I < 0:
            return 0
        return T1[I]

    def DP2(J):
        if J < 0:
            return 0
        return T2[J]

    def DP3(I, J):
        if I < 0 or J < 0:
            return 0
        return T3[I, J]

    def recur(I, J): 
        
        pass

    pass


def main():
    pass


if __name__ == "__main__":
    main()