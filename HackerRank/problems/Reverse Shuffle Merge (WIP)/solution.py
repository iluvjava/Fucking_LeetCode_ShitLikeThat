def reverse_shuffle_merge(s):
    """
        This is just for creating some inputs for investigations. 
    """
    from random import shuffle
    from random import random
    ShuffledSymbols = [C for C in s]
    shuffle(ShuffledSymbols)
    Reversed = list(reversed(s))
    def SubRoutine():
        Merged = ""
        I = J = 0
        while I < len(s) and J < len(s):
            if int(random()*2) == 1:
                Merged += ShuffledSymbols[I]
                I += 1
            else:
                Merged += Reversed[J]
                J += 1

        while I < len(s) or J < len(s):
            if I < len(s):
                Merged += ShuffledSymbols[I]
                I += 1
            if J < len(s):
                Merged += Reversed[J]
                J += 1
        return Merged

    Merged = SubRoutine()
    return Merged, "".join(ShuffledSymbols), "".join(Reversed)


def solution_failed(s):
    s = list(reversed(s))
    from collections import Counter
    MtiSet = Counter(s)

    print(f"Reversed Merged: {''.join(s)}")

    def SubsequenceMultiset():     
        MtiSetInner = MtiSet.copy()  # bring to inner scope
        MtiSetList = [MtiSetInner.copy()]
        for C in s:
            MtiSetInner[C] -= 1
            if MtiSetInner[C] == 0:
                del MtiSetInner[C]
            MtiSetList.append(MtiSetInner.copy())
        return MtiSetList

    MtiSetList = SubsequenceMultiset()
    
    def SubseqExists(I, MtiSet, Threshold=0):
        """
            I is inclusive.
        """
        Subseq = MtiSetList[max(I, Threshold)]
        
        for K, V in MtiSet.items(): 
            if K not in Subseq and Subseq[K] < V:
                return False
        return True

    # print(MtiSetList)

    def IdentifySymbols():
        Symbols = dict([(K, V//2) for K,V in MtiSet.copy().items()])
        return Symbols, sorted(list(Symbols.keys()))
    
    Symbols, Keys = IdentifySymbols()  # Symbol is a multi-set. 

    print(f"Symbols: {Symbols}")
    print(f"Keys: {Keys}")

    Res = ""
    Threshold = 0
    while len(Keys) > 1 or Symbols[Keys[0]] > 1:
        
        for K in Keys:
            
            print(f"Looking at {K}")
            print(f"Remainging choices: {Symbols}")
            Loc = s.index(K, Threshold)
            if SubseqExists(Loc, Symbols):
                Res += K
                Threshold = Loc + 1
                print(f"Added, res: {Res}")
                if Symbols[K] == 1:
                    del Symbols[K]
                    Keys.remove(K)
                else:
                    Symbols[K] -= 1
                break
            else:
                # um... do nothing and skip to the next character in Keys
                pass
    Res += Keys[0]
    return Res


def solution_working_but_slow(s):
    from collections import Counter
    s = list(reversed(s))
    
    def IdentifySymbols():
        Symbols = sorted(s)[::2]
        return Symbols

    def GetMultiSetList():
        GrandMultiset = Counter(s)
        MsetList = [GrandMultiset]

    Symbols = IdentifySymbols()

    def SubseqIn(I, Symbols):
        
        MultiSet1 = Counter(s[I:])
        MultiSet2 = Counter(Symbols)
        # check MultiSet2 is a subset of MultiSet1
        for K, V in MultiSet2.items():
            if K not in MultiSet1 or MultiSet1[K] < V:
                return False
        return True
    
    Res = ""
    while len(Symbols) > 1:
        for S in Symbols:
            Loc = s.index(S)
            if SubseqIn(Loc, Symbols):
                s = s[Loc + 1:]
                Symbols.remove(S)
                Res += S
                break
    Res += Symbols[0]
    return Res


def solution(s):
    from collections import Counter
    s = list(reversed(s))
    
    def IdentifySymbols():
        Symbols = sorted(s)[::2]
        return Symbols

    def GetMultiSetList():
        GrandMultiset = Counter(s)
        MsetList = [GrandMultiset]
        PreMset = GrandMultiset
        for C in s:
            NextMset = PreMset.copy()
            NextMset[C] -= 1
            PreMset = NextMset
            MsetList.append(NextMset)
        return MsetList

    Symbols = IdentifySymbols()
    MsetList = GetMultiSetList()

    def SubseqIn(I, Symbols):
        MultiSet1 = MsetList[I]
        MultiSet2 = Counter(Symbols)
        # check MultiSet2 is a subset of MultiSet1
        for K, V in MultiSet2.items():
            if K not in MultiSet1 or MultiSet1[K] < V:
                return False
        return True

    Res = ""
    LocAccumlate = 0
    while len(Symbols) > 1:
        for S in Symbols:
            Loc = s.index(S)
            if SubseqIn(LocAccumlate + Loc, Symbols):
                s = s[Loc + 1:]
                LocAccumlate += Loc + 1
                Symbols.remove(S)
                Res += S
                break
            
    Res += Symbols[0]
    return Res



def main():
    def RandomTest():
        for _ in range(100):
            Merged, Shuffled, Reversed = reverse_shuffle_merge("abcd")
            print(f"Merged: {Merged}")
            Soln = solution(Merged)
            print(f"Soln is {Soln}")
            # assert Soln == "abcde", "ono"
    def Test1():
        Merged = "abcdefgabcdefg"
        print(f"Merged: {Merged}")
        Soln = solution(Merged)
        print(f"soln: {Soln}")

    def HiddenTest():
        Inputs = "bdabaceadaedaaaeaecdeadababdbeaeeacacaba"
        Expected = "aaaaaabaaceededecbdb"
        Soln = solution(Inputs)
        print(f"Soln: {Soln}")
        print(f"Expected: {Expected}")
        
    Test1()
    # RandomTest()
    HiddenTest()
    
if __name__ == "__main__":
    main()
