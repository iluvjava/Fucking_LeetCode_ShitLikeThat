# Problem Statement:

* Give 2 string with different length, what is the minimum number of deletions of characters such that it makes both
string to be anagram of each other.

* Operations:
  * deletion of a characters from one of the string.

  * Given: cde, abc, delete `de` from cde to get c, delete `ab` from `abc` to get c

  * model each string as a frequencies map, consider a set of characters that are the unions of characters from both
  string, name it `S`
```
  DeletionCounter = 0
  foreach(Character c in S):
    if (c presents in both string):
      take the absolute difference of the frequencies of that characters in string1, string2
      DeletionCounter += The difference get from the string
    else:
      take the frequencies of that characters in the string that it's in.  
      DeletionCounter += The frequencies that the character has in whichever string it's in. 
```