def soln_Dead1(arr, r):
    Max = max(arr)
    FreqDic = {}
    GeoSeq = set()
    G = 1

    while G <= Max:
        GeoSeq.add(G)
        G *= r
    del G  # name scape polution.
    Counter = 0
    for I in reversed(arr):
        if I in GeoSeq:
            if I not in FreqDic:
                FreqDic[I] = 1
            else:
                FreqDic[I] += 1
            Counter += FreqDic.get(I*r, 0)*FreqDic.get(I*r*r, 0)
    return Counter


def soln_dead2(arr, r):
    FreqDic = {}
    Counter = 0
    for I in reversed(arr):
        if I not in FreqDic:
            FreqDic[I] = 1
        else:
            FreqDic[I] += 1
        Counter += FreqDic.get(I*r, 0)*FreqDic.get(I*r*r, 0)
    return Counter


def soln(arr, r):
    FreqTable, TupleFreq = {}, {}
    Counter = 0
    for X in reversed(arr):
        Counter += TupleFreq.get(X, 0)
        if X//r != 0:
            if X//r in TupleFreq:
                TupleFreq[X//r] += FreqTable.get(X*r, 0)
            else:
                TupleFreq[X//r] = FreqTable.get(X*r, 0)
        FreqTable[X] = FreqTable.get(X, 0) + 1
    return Counter
        

def wrap(arr, a):
    return soln(list(map(int, arr.split())), a)


def wrap_soln_dead(arr, a):
    return soln_Dead1(list(map(int, arr.split())), a)


def wrap_soln(arr, a):
    return soln_dead2(list(map(int, arr.split())), a)


def main():

    def hidden_testcases(hidden):
        Lines = None
        with open(hidden) as f:
            Lines = f.readlines()
        Expected = Lines[0].split()[0]
        print(f"Expected: {Expected}")
        print(f"Actually get: {wrap(Lines[1], int(Lines[0].split()[1]))}")
        print(f"Dead gives: {wrap_soln_dead(Lines[1], int(Lines[0].split()[1]))}")

    print(wrap("1 2 2 4", 2))
    print(wrap("1 3 9 9 27 81", 3))
    hidden_testcases("hidden_testcase6.txt")
    


if __name__ == "__main__":
    main()