def solution(s, t):
    if s == t: return True
    if len(s) != len(t): return False
    Mapper = {}
    for C1, C2 in zip(s, t):
        if C1 in Mapper:
            return False
        else:
            Mapper[C1] = C2
    
    pass


def main():
    pass


if __name__ == "__main__":
    main()