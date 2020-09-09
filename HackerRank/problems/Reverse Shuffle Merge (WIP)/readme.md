# Problem statement

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

* Note this problem is hard and we might need some kind of proof to justify what we are doing.

### Let's do an example

* 233211 = merge(shuffle("123"), reverse("123")), original = ???

* From the output, 233211 we know that, the symbols involved for the strings are: `s = {1, 2, 3}`
  * Greedily, we want the lowest lexigraphical ordering of the original string, hence, it's reverse order should
  preferably start with the biggest element in the set.

  * Can the reversed(original) start with 3? yes, because, 1, 2 comes after it, and in that sense, it's a valid.

  * Can the second element of reversed(original) be 2? yes, 1 comes after it, hence, it's valid.

  * Then, we know that, reversed(original) can be 321, and that means, original = 123, and it's the lowest lexicalgraphic
  ordering of all permutations.

* abcdefgabcdefg = merge(shuffle(???),reverse(???))
  * Identifying the set of elements for the string, we sort it, and extract the set of symbols that can makes the stirng
  * 'aabbccddeeffgg', all elements the elements are repeated 2k times.
    * Set: {a, b, c, d, e, f, g}
  * We want reversed(???) to end with a, so it's lexicographically as small as possible.
    * Find the symbol `a` such that all the elements except `a` comes before `s` in the array.
    * Choose: `abcdefg(a)bcdefg`, the first appearance of a in the sequence indeed, has the property that, all the
    other symbols comes after it.
