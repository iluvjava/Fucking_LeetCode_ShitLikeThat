# Problem statement.

* Intro:
  * We defined a set of operations that is applied to the string, and then applied it to a given string,
  and we want to find a string that, after that sequence of operations, produce the original string in such a way
  that, the original string has the minimum legxicalgraphic order among the space of all possible string.

* The set of operations:
  * Random Permutations: Shuffle
  * Reverse.
  * Merge:
    * Merge(A, B), where A, B are 2 string, produces string C, such that:
      * There eixsts 2 subsequences of the C where, it's the same as string A, and string B, and they made up the
      whole string C.

* Input: String s, where `s in merge(per(A), reverse(A))`.

* Find that string A, that with the smallest Lexical graphical order.

