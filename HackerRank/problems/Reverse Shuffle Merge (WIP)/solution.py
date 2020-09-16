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



def main():
    print(reverse_shuffle_merge("4312"))
    
if __name__ == "__main__":
    main()
