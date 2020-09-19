# Problem Statement 

* A sequence of characters, a-z is given, sort it in decreasing order of the letter's frequencies. 

```
    Input:
    "tree"

    Output:
    "eert"

    Explanation:
    'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

```

* Note: Swapping letters with the same frequencies will still count as a valid solution to the problem. 

### Strategies

* Get the frequencies mapping for letters. 

* Reverse the map, sort all the frequencies for the lettter

* Concate them to form the results.

### Choice of Language

* For this problem python is chosen because all the data structures needed for 
the solution is in the python std library. 

