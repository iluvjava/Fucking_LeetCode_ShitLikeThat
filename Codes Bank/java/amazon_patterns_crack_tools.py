"""
    Tool is made with the intention of making the amazing interview 
    24 reasoning problem easier. 
"""

__all__ = ["patterns_filter"]

import re 

def patterns_filter(before, after):
    """
        before and after are string with the following formats: 
          * All capitalized letters. 
          * All numbers. 
          * A combinations of the above. 
    
    """
    
    def RelativeRanksTransform(theString):
        SmallestChar = sorted(list(theString))[0]
        return [ord(C) - ord(SmallestChar) for C in theString]

    # --- Both Strings are consists of capital letters. --------------------------------------------
    if re.match("^[A-Z]+$", before) and re.match("^[A-Z]+$", after):
        print("Both strings are consist of capitalized letters. ")

        BeforeNumList = [ord(C) - ord("A") for C in before]
        AfterNumList = [ord(C) - ord("A") for C in after]
        
        print("ElementWise Ordinality Difference: ")
        print([A - B for B, A in zip(BeforeNumList, AfterNumList)])
        
        print("Are 2 string Anagram of each other? ")
        print(set(before) == set(after))
        
        print("Are BOTH String made of consecutive letters? ")
        BeforeLettersSorted = sorted([C for C in before])
        AfterLettersSorted = sorted([C for C in after])
        if ord(BeforeLettersSorted[-1]) - ord(BeforeLettersSorted[0]) == len(BeforeLettersSorted)\
            and\
                ord(AfterLettersSorted[-1]) - ord(AfterLettersSorted[0]) == len(AfterLettersSorted):
            print("Yes")
            print("And let's get the mapping too.")
            print(RelativeRanksTransform(before))
        else: 
            print("NO")
    
    
    


def main():
    pass


