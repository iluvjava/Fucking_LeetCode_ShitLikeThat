# Problem statement.

* (link)[https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming]

* The problem is interested in operating with string. 

* Generally speaking, it's doing the following: 
  * Given some kinda of allowed string operations, determinie if it's possible to convert one string 
  to another given string under the set of operations. 

* Operations allowed: Delete or capitalize a letter in the world. 
  
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

#### The algorithm

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

#### Warning: 

* This algorithm might not be optimal, because as we know, if there eixsts a letter in B that is not
part of A, then the output is automatically false. 
  * However, for the borrowed algorithm, that is not determined until the table has been constructed


# Idea2 (Modifed Longest Common Substrin algorithm)

* Fact: letters in B is a sub-set of letters in A. 
  * For [i, j] pair in A, B, letter in A can be skipped but letter in B cannot be skipped.

* define T, T[I, J] := "It's possible that, using the substring a[J: I+1], we can reduce it to the 
substring B[: J + 1]."

* T[I, J] := T[I - 1, J - 1] + 1 if A[I].capitalize() == B[J]





