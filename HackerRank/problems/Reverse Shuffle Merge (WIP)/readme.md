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

  * Then, we know that, reversed(original) can be 321, and that means, original = 123, and it's the lowest
  lexicographic ordering of all permutations.

* abcdefgabcdefg = merge(shuffle(???),reverse(???))
  * Identifying the set of elements for the string, we sort it, and extract the set of symbols that can makes the stirng
  * 'aabbccddeeffgg', all elements the elements are repeated 2k times.
    * Set: {a, b, c, d, e, f, g}
  * We want reversed(???) to end with a, so it's lexicographically as small as possible.
    * Find the symbol `a` such that all the elements except `a` comes before `a` in the array.
    * Choose: `abcdefg(a)bcdefg`, the first appearance of a in the sequence indeed, has the property that, all the
    other symbols comes after it.

#### A observation

* Just reverse the input string, because we don't care about the shuffled subsequence in the input of the string
anyway.

* yeah... in that case, we are off with one of the weird constraint and we can focuses on the **Subsequence that is
reading from left to right, not right to left** making the jobs for our brain easier.

#### Another Example

* 2241435531 = merge(shuffle(35142), reverse(35142)), Lowest Lexicalgraphic Original?

* Because we don't care about the suffled sub-sequence, we are going to just reverse the whole string, then the
following can be said:

* 1355341422 = merge(shuffle(?), ?).

* Among all possible sequences that can be made into that particular sequence after the operation, we want to
find the one with the lowest lexicalgrphic order.

* Fact: The sequence we wanna search have the following set of symbols:
  * {1, 2, 3, 4, 5}, when put into lexigraphic ordering.

* Can ? start with 1?
  * (1)35534(1)422, choose the frist appearance of 1, all remaining characters we good
  * Then ? = 1...
* Can ? continues with 2?
  * 13553414(22), no, because 3, 4, 5, 6, doesn't come after 2 in this sequence.
  * ? = 1... still
* Can ? continues with 3?
  * 1(3)55(3)41422, yes, 2, 4, 5, comes after the first 3.
  * ? = 13...
* Can ? continues with 4?
  * 13553(4)1(4)22, no, for both option, 2, 5 doesn't come after it.
  * ? = 13...
* Can ? continues with 5?
  * 13(55)341422, yes, 2 and 4 comes after it.
  * ? = 135...
* Can ? continues with 2?
  * 13553414(22), no,  doesn't come after it.
  * ? = 135...
* Can ? continues with 4?
  * 13553(4)1(4)22, yes, 2 comes after it and it's the last option to choose for the unknown string?
  * ? = 13542

* The minimum lexicalgraphic ordering of the strign should be 13542, (135)53(4)14(2)2.

#### Let's Do another Example

* 12134432 is the input. then we know that: 23443121 = merge(shuff(A), A), then we want to look for the same A, that
is minimum in lexical order.

* Identify the set of symbols that make up A, which is: {1, 2, 3, 4}, sorted in alphebetical order.

* For each of the symbol, we query in a greedy manner, to try to make it, a legit subsequence of the input sequence
of symbols.

* Remaining Symbols in sorted order: R = {1, 2, 3, 4}
  * consider 1, 23443(1)2(1), no, not possible
  * consider 2, (2)3443121, yes, choose 2
    * A = 2..., R = {1, 3, 4}
* R = {1, 3, 4}, A = 2...
  * consider 1, 23443(1)21, no, not possible
  * consider 3, 2344(3)121, no, 1 and 4 doesn't comes after it.
  * consider 4, 23(4)43121, yes, 1, 3 comes after it, choose 4
    * A = 24..., R = {1, 3}

* R = {1, 3}, A = 24...
  * consider 1, 23443(1)21, no, 3 doesn't come after it.
  * consider 3, 2344(3)121, yes, 1 come afer it. Choose 3
    * A = 243..., R = {1}

* There is only one character left in R, then, just make A = 2431.

* Then, (1)21(34)43(2) = merge(shuffle(2431), reverse(2431)).

#### Let's summarized what we did, trying to reduce it to an algorithm. 

* 