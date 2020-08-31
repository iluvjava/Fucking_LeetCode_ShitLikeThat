def solution(k, c):
    c.sort(reverse=True)
    Groups = []
    for I in range(0, len(c)//k + 1):
        Groups.append(c[I*k: min(I*k + k, len(c))])
    RunningSum = 0
    for I, G in enumerate(Groups):
        RunningSum += sum(G)*(I + 1)
    return RunningSum

def main():
    print(solution(3, [1, 3, 5, 7, 9]))
    pass


if __name__ == "__main__":
    main()