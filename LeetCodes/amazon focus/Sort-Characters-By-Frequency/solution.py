

def solution(s):
    # Frequencies --------------------------------------------------------------
    from collections import Counter
    Freq = Counter(s)
    
    # Reversed Maping ----------------------------------------------------------
    ReversedMap = {}
    for Letter, Frq in Freq.items():
        TheList = ReversedMap.get(Frq, [])
        TheList.append(Letter)
        ReversedMap[Frq] = TheList

    # Sort the list of Frequencies ---------------------------------------------
    SortedFreq = sorted(list(ReversedMap.keys()), reverse=True)
    ResString = ""
    for F in SortedFreq:
        ListofLetters = ReversedMap[F]
        ListofLetters = "".join([L*F for L in ListofLetters])
        ResString += ListofLetters
    
    return ResString


def main():
    print(solution("Tree"))
    print(solution("everymomentifeelmyselfdisintegratedintovoid"))


if __name__ == "__main__":
    main()