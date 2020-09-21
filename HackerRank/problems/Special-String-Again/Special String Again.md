# Problem Statement

* For this problem we are insterested in a special type of palimdrone.
  * aaabaaa, odd letters, and the middle one is any character while all the other characters the the same.
  * aaaaaa, all characters are the same.

* Input given any string.

  * among all possible substring of the given string, count the number of substrings that is a spcial type of
  string.

* Output: an integer.

## Dynamic Programming (FAILED)

* The Secret Mantra: Optimal Structure...
  * let `s` denote the substring that is given to us.
  * consider any substring, `s[I, J + 1]`, and relation to its substring.
    * if `s[I, J + 1]` is a special string, then:
      * `s[I - 1, J]` is a special string, and `s[I - 1] == s[J - 1]`

### Let's Investigate Some Sxamples

* "mnonopoo" has the following special substrings:
  * {m, n, o, n, o, p, o, o, non, ono, opo, oo}

* Base Cases:
  * Single letters are special string.
  * Empty string is a special string.

* Complexity:
  * If we just do a search on the whole solution space, then it's 2d, which is O(N^2), because parametric bound.

## Random Idea

* Consider the fact that there are only 26 letters in the alphabet, there might be something we can exploit there...

* Big O(N^2) solution is fundementally infeasible because of the size of the inputs from the hidden testcase.

* If "aaaa" is a special substring, it's even, then all its substrings are special.

### Use a Stack

* So we add elements into the stack and count the total number of substrings.
  * a: +1 special substring
  * a: +2 special substring
  * a: +3 special substring
  * b: +1 special substring
  * a: +2 special substring

* Ok, cunting it one by one while traversing through the array might not be that good of an idea, let's try to exploit
some optimal structures of the problem.

* let T[I, J] denotes the number of special string included in the substring s[I, J + 1].
  * the string s[I, J + 1] consists of s[I + 1, J + 1] and s[I, J].

* Ok we beed to know what type of special string it is exactly in order to know how to combine the optimal solutions.

### Exploit the properties of the special substring

* TypeI Special String: "All letters are the same"
  * total number of substring: L = len(s); (L*(L - 1))/2

* TypeII Special String: "All letters are the same, except the middle one, and it has odd length"
  * Say: L = 2*K + 1, then K^2 is the number of special subtring of this string. 

## Algorithm (Expoit Properties and use Tuple array)

* mnonopoo -> [(m, 1), (n, 1), (o, 1), (n, 1), (o, 1), (p, 1), (o, 2)]

* First, find all the type I special string.
  * 9 of them.

* Find all type II string, we will need 3 pointers for it.
  * non, ono, opo --> +1, + 1, + 1  --> 3 + 9 = 12 of them in total.


```python
def substrCount(n, s):
    total = n
    for i in range(n):
        count = 1
        for j in range(i + 1, n):
            if (s[i] == s[j]):
                count += 1
                total += 1
            else:
                size_of_palindrome = count * 2 + 1
                if (i + size_of_palindrome <= n and s[i:i + size_of_palindrome] == (s[i] * count) + s[j] + (s[i] * count)):
                    total += 1
                break
    return total
```