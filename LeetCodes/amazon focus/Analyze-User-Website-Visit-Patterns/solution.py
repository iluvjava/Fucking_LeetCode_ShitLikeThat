def solution(userName, timeStamp, website):
    # Get the (timestamp, website) tuple for each of the user --------------------------------------
    TimeStampWebsite = {}
    for Name, Time, Website in zip(userName, timeStamp, website):
        TupleList = TimeStampWebsite.get(Name, [])
        TupleList.append((Time, Website))
        TimeStampWebsite[Name] = TupleList

    User2WebsitesTriples = {}
    AllTriples = set()
    # Sort all the website they visited by the time stamp ------------------------------------------
    for Name, TupleList in TimeStampWebsite.items():
        TupleList.sort(key=lambda x: x[0])
        TupleList = [E[1] for E in TupleList]
        Triples = set()
        for I in range(len(TupleList)):
            for J in range(I + 1, len(TupleList)):
                for K in range(J + 1, len(TupleList)):
                    Triples.add((f"{TupleList[I]},{TupleList[J]},{TupleList[K]}"))
        AllTriples |= Triples
        User2WebsitesTriples[Name] = Triples

    print(f"User to websites {User2WebsitesTriples}")
    # For each user, create a set of triplets sequences. 
    Triplets2Freq = {}
    for Triple in AllTriples:
        Count = 0
        for UserTripleSet in User2WebsitesTriples.values():
            if Triple in UserTripleSet:
                Count += 1
        Triplets2Freq[Triple] = Count
    print(f"Triple to Frequency: {Triplets2Freq}")
    Maxcount = max(list(Triplets2Freq.values()))
    Ans = [T for T, F in Triplets2Freq.items() if F == Maxcount]
    Ans.sort()
    return Ans[0].split(",")
 

def main():
    
    pass


if __name__ == "__main__":
    main()