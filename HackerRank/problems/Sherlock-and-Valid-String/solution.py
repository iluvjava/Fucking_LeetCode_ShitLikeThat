def solution(s):
    from collections import Counter
    F = Counter(s)
    FF = Counter(F.values())
    if len(FF.keys()) == 1:
        return "YES"
    if len(FF.keys()) > 2:
        return "NO"
    Flarger = max(FF.keys()); Fsmaller = min(FF.keys())
    if FF[Flarger] == 1 and Flarger - Fsmaller == 1:
        return "YES"
    if FF[Fsmaller] == 1:
        return "YES"
    return "NO"


def main():
    print(solution("aabbcd"))
    print(solution("abcddd"))
    print(solution("aabbccc"))
    pass


if __name__ == "__main__":
    main()