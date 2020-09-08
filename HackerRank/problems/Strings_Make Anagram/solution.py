def solution(s1, s2):
    from collections import Counter
    FreqMap1, FreqMap2 = Counter(s1), Counter(s2)
    AllCharacters = set(s1) | set(s2)
    DeletionCounter = 0
    for C in AllCharacters:
        if C in FreqMap1 and C in FreqMap2:
            DeletionCounter += abs(FreqMap1[C] - FreqMap2[C])
        else:
            DeletionCounter += FreqMap1.get(C, 0) + FreqMap2.get(C, 0)
    return DeletionCounter


def main():
    print(solution("abc", "cde"))
    
if __name__ == "__main__":
    main()