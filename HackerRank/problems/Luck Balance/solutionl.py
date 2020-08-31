
def solution(k, rows):
    ImportantContests, Unimportantcontests = [], []
    for R in rows: 
        if R[1] == 1:
            ImportantContests.append(R[0])
        else:
            Unimportantcontests.append(R[0])
    ImportantContests.sort(reverse=True)
    LuckyPoints = 0
    for I in range(min(k, len(ImportantContests))):
        LuckyPoints += ImportantContests[I]
    if k < len(ImportantContests):
        for I in range(k, len(ImportantContests)):
            LuckyPoints -= ImportantContests[I]
    return sum(L for L in Unimportantcontests) + LuckyPoints


def main():
    arr =  [[5  ,1],
            [2  ,1],
            [1  ,1],
            [8  ,1],
            [10 ,0],
            [5  ,0]]
    k = 3
    print(solution(k, arr))
    

if __name__ == "__main__":
    main()