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






def solution_working_but_slow_still(s):
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


class OrderedMultiSet:

    """
        Created with the purpose of storing the symbols set for the sequence for the problem.
        * This is going to be an iterator.
        * This is going to support subset operation.
        * Supports removal of one element at a time while iterating through.
        Author: Alto
    """

    def __init__(self, allSymbols):
        """
            Construct the multi set from a list of symbols
        """
        from collections import Counter
        MultiSet = Counter(allSymbols)
        SortedUniqueSymbols = sorted(list(set(allSymbols)))
        self._Cardinality = len(allSymbols)
        self._MtSet = MultiSet
        self._Symbols = SortedUniqueSymbols
        self._Pointer = (0, 0)  # Pointing the the element that is going to be returned in the multiset.
        self._Toreturn = None  # A back for the element to return, so that, we don't have array out of index when the
        # element is removed immediately after the use of .next().
        self._PrePointer = None  # Pointing at the element that is going to be returned by the next call of next()
        """
            self._Pointer: 
              This is the future pointer, it might, or might not point to a valid value, this is true because, 
              after the remove() has been called, it might failed to point to anything, that is where, self._Toreturn
              comes in. 
            
            self._Toreturn:
              This is a back up, when next() is called, it prepare the next value that is is going to be returned 
              next time in advance, to prevent self._Pointer to be pointing into invalid places, and self._Pointer
              will be reset to a valid pointer once the function next() is done. 
              
            self._PrePointer: 
              When removing the element that was returned by next(), we need to know which element it is, and that is 
              what this variable is for.
              Just goes to the this pointer in the multi-set and remove the element, or decremenet the frequency of the 
              element accordingly. 
        """

    def reset_itr(self):
        self._Pointer = (0, 0)
        self._Toreturn = None
        self._PrePointer = None

    def remove(self):
        """
            Remove the most recent element that is returned by the next() method.
            * The pointer is pointing at the future element, not the most recent element
        """
        assert self._PrePointer is not None, "Can't remove when you haven't called next()"
        ToRemoveIdx, _= self._PrePointer
        ToRemoveElement = self._Symbols[ToRemoveIdx]
        if self._MtSet[ToRemoveElement] == 1:
            del self._MtSet[self._Symbols[ToRemoveIdx]]
            self._Symbols.pop(ToRemoveIdx)
        else:
            self._MtSet[ToRemoveElement] -= 1

        self._Cardinality -= 1

    def next(self):
        """
            Returns the current element from from the multiset.
            * Return current element, move the pointer to the next element.
        """
        assert self.has_next(), "can't get next when it's the last one"
        P1, P2 = self._Pointer
        self._PrePointer = self._Pointer
        Results = self._Symbols[P1]
        if P2 >= self._MtSet[P1]:
            self._Pointer = (P1 + 1, 0)
        else:
            self._Pointer = (P1, P2 + 1)
        # Pointer has been advanced
        if self._Pointer[0] <= len(self._Symbols) - 1:
            self._Toreturn = self._Symbols[self._Pointer[0]]
        else:
            self._Toreturn = None  # no more elements folks, I am sorry.
        return Results

    def has_next(self):
        P1, F1 = self._Pointer
        if P1 >= len(self._Symbols):
            return False
        if self._MtSet[P1] > F1:
            return P1 < len(self._Symbols) - 1
        if P1 >= len(self._Symbols) - 1:
            return F1 < self._MtSet[self._Symbols[P1]]

        return True

    def subset_of(self, other):
        for K, V in self._MtSet.items():
            if K not in other or other[K] < self._MtSet[K]:
                return False
        return True

    @property
    def Cardinality(self):
        return self._Cardinality

    def __repr__(self):
        return str(dict(self._MtSet))


def solution(s):
    from collections import Counter
    def IdentifySymbols(s):
        Symbols = sorted(s)[::2]
        return OrderedMultiSet(Symbols)
    
    Symbols = IdentifySymbols(list(reversed(s)))
    print(f"Symbols Extracted as Multi-Set: {Symbols}")
    
    def GetMultiSetList(s):
        s = "".join(reversed(s))
        GrandMultiset = Counter(s)
        TheSequence = s
        MsetList = [GrandMultiset]
        PreMset = GrandMultiset
        for C in s:
            NextMset = PreMset.copy()
            NextMset[C] -= 1
            PreMset = NextMset
            MsetList.append(NextMset)
        SubSequenceMultiSet = {}
        for I in range(len(TheSequence)):
            SubSequenceMultiSet[TheSequence[I:]] = MsetList[I]
        SubSequenceMultiSet[""] = MsetList[-1]
        return SubSequenceMultiSet

    MultisetSubseq = GetMultiSetList(s)
    for K, V in MultisetSubseq.items():
        print(f"{K} ===> {V}")

    s = "".join(list(reversed(s)))
    Substring = s
    Res = ""
    while Symbols.Cardinality > 0:
        print(f"Symbols Mset: {Symbols}")
        print(f"Substring: {Substring}")
        while Symbols.has_next():
            Token = Symbols.next()
            print(f"Looking at Token: {Token}")
            Loc = Substring.find(Token)
            if Symbols.subset_of(MultisetSubseq[Substring[Loc:]]):
                print(f"Update Res: {Res}")
                Res += Token
                Symbols.remove()
                Substring = Substring[Loc + 1:]
                break
        Symbols.reset_itr()
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
