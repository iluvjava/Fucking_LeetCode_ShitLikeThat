def freqQuery(queries):
    """
        We are keeping track of a compsite mapping throughout the queries, 
        and here is the mapping we are keeping track of: 
        
        Element |--> Freq |--> # of element with that Freq
    """
    Res = []
    Ele2Freq = {}
    Freq2ElementCount ={}

    def ElementFreqTrackAdd(FreqTbl, Element):
        if Element in FreqTbl: 
            FreqTbl[Element] += 1
        else: 
            FreqTbl[Element] = 1
        return

    def ElementFreqTrackRemove(FreqTbl, Element):
        if Element not in FreqTbl: 
            return
        FreqTbl[Element] -= 1
        if FreqTbl[Element] == 0:
            del FreqTbl[Element]
        return
        
    for Opt, Element in queries:
        if Opt == 1: 
            ElementFreqTrackAdd(Ele2Freq, Element)
            ElementFreqTrackAdd(Freq2ElementCount, Ele2Freq[Element])
            ElementFreqTrackRemove(Freq2ElementCount, Ele2Freq[Element] - 1)
        elif Opt == 2:
            if Element in Ele2Freq:
                ElementFreqTrackRemove(Freq2ElementCount, Ele2Freq[Element])
                if Ele2Freq[Element] - 1 != 0:
                    ElementFreqTrackAdd(Freq2ElementCount, Ele2Freq[Element] - 1)
                ElementFreqTrackRemove(Ele2Freq, Element)
        else:
            Res.append(1 if Element in Freq2ElementCount else 0)
        pass

    return Res
