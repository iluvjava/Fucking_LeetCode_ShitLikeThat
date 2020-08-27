# Problem statement.

* (link)[https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming]

* The problem is interested in operating with string.

* Generally speaking, it's doing the following:
  * Given some kinda of allowed string operations, determinie if it's possible to convert one string
  to another given string under the set of operations.

* Operations allowed:
  * capitalize a **LOWER CASED** letter in the word A.
  * Delete all of the remaining **Lower Cased** Letter in A.

  * Given string A, B, determine if it's possible to convert string `A` to `B` with the given
  set of operations.

## Idea 1 (Longest Common Subsequence Borrowed)

* Borrow the algorithm for longest common subsequence for this problem.
  * The longest common subsequence between A, B must be B.
    * If not, then there eixsts symbol in B that is not in A, the set of operations only reduce
    sequence A, hence, impossible to convert.
  * If such a Longest Common Subsequence is found, then for all letter `L` in the LCSeq that is
  capitalized, the corresponding letter in B must also be capitalized.
    * If the exists a letter `l` in LCseq that is capitalized but the correspodning `l` in B is
    not, then there doesn't exists an operations that convert A to B.

### The algorithm

* let T[I, J] := "Integer, longest common subsequence between A, B using the first I symbols of
A and the first J elements of B, including the I, J th index. "

* For this problem, we also need to store what the substring is, so at each [i, j], a letter must
be included..., or "how the decision is made must also be inclued."

* For each [i, j], the following cases can happen:
  * if A[i] == B[j], then the longest common subfix increases. T[i, j] := T[i - 1, j - 1] + 1
  * if A[i] != B[j], then the longest commob subfix is like:
  T[i, j] := max(T[i - 1, j], T[i, j - 1])

* Define another tale, T2[I, J]:= "The type of decision is made during the making of table T."
  * it should have the following values:
    * 1: T[i, j] := T[i - 1, j - 1] + 1 is chosen
    * 2: T[i, j] := T[i - 1, j] is chosen
    * 3: T[i, j] := T[i, j - 1] is chosen

* Feels like a 2d prefix sum for some reasons.

* Recovering the table and get the LCSeq

### Warning

* This algorithm might not be optimal, because as we know, if there eixsts a letter in B that is not
part of A, then the output is automatically false.
  * However, for the borrowed algorithm, that is not determined until the table has been constructed

## Idea2 (Modifed Longest Common Substrin algorithm)

* Fact: letters in B is a sub-set of letters in A.
  * For [i, j] pair in A, B, letter in A can be skipped but letter in B cannot be skipped.

* define T, T[I, J] := "the number of letters such that, using the substring A[J: I + 1], we can reduce it to the
substring B[: J + 1] with the given string operations"

* T[I, J] := (T[I - 1, J - 1] + 1) if (A[I].capitalize() or A[I] == B[J]) else SKIP to next case

* When skipping the letter in I th letter in A:
  * T[I, J] = T[I - 1, J] or T[I, J -1] depending on which one has a bigger value.

* Base case:
  * T[-1, ?] = T[?, -1] = T[-1, -1] = True

* Let's fucking do it by hands first before coding this shit out.

```python
A = "AbcDE", B = "ABDE"

Bool matrix
  A b c D E
A 1 1 1 1 1
B 0 2 2 2 2
D 0 2 2 3 3
E 0 2 2 3 4

LCS: AbDE
```

* Yes, because the longest common capitalized subsequence has the same length as B

```python
A = "AfPZN", B = "APZNC"

Bool Matrix
  A f P Z N
A 1 1 1 1 1
P 0 1 2 2 2
Z 0 1 1 3 3
N 0 1 1 3 4
C 0 1 1 1 4

LCS: APZN
```

* No, 4 is less than the length of the string B.

```python
A, B = "beFgH", "EFG"

  b e F g H
E 0 1 1 1 1
F 0 1 2 2 2
G 0 1 2 3 3

  b e F g H
E T T F F F
F
G
```

* Expected to be False...

* The LCS: eFg, expected False because:
  * "H", "b" in `B` are deleted, and one of them is not a lower cased letter.

### Something Extra

  * We might need to keep track of **the sequence of letters** in `A` that made its way to construct the string `B`.

```
foreach(letter: L not in LCS):
  L must be lower.
```

### Still failed

* There are multiple LCS, some of them may be valid, some of the might not.

## Idea 3 (Modifed LCS but with Boolean Matrix)

* T[I, J] := "It is possible that, there exists a sequence of operations that map subtring A[: I + 1] to B[:J + 1]. "
* Set of Operations;
  * Capitalized a lowercased letter in A.
  * Delete all Lowercased Letter in A.

* Consider any T[I, J]
  * Then A[I] is either an upper case letter, or a lower case letter.
  * if A[I] is Upper:
    * if A[I] != B[J]: Cannot Deleted A[I]. T[I, J] = T[I, J - 1]
    * else it's equal, still cannot delete it because it's capitalized: T[I, J] := T[I - 1, J - 1]
  * if A[I] is Lower:
    * Delete A[I]: T[I, J] = T[I - 1, J]
    * Capitalize A[I]: T[I, J] = T[I - 1, J - 1] and (A[I].upper() == B[J])

* Define Base case:
  * T[-1, ?] = T[?, -1] = True



## Idea 4, (Recursion with Memeorization)

* For each non-cap letter in A, we have the choice to either ignore it, or 
to capitalize it.

* The base case is that, if 2 string B is empty, and all the letters in string A
is lower cased (can be removed), then it's a match! A is empty also means a 
mathc. 

