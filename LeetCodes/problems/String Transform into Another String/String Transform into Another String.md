## Problem Statement

* Given 2 string, and we allow the operation of changing all the occurence of one letter in the alphabet to another, determine whether it's possible to transform one string into another using such a transformation (or not using an operations at all if they are alread the same)

* Let's look at an example
```
Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
```

```
Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
```

### Discussion
* Notice how, similar string all share the same patterns on with the same occurences of letters in the string.
* How do we identiy string having the same patterns? We are probably gonna be using numbers instead of letters then.
* Consider the case where all the letters in the string is unique, then, there will always exist a set of operations that lead to one string to the other, because, can change each letter in one string to match the other one.
* Take the example of "ccdee", when a letter first appeared, we assign a new id for it, and when it appeared a second time, we assign the original ID of the letter, we do that and convert the string into:
	* "ccdee" ---> 11233
   * "aabcc" ---> 11233
   * Boom! they got mapped to the same number... Intersting interesting...
* or for fun we can make use another special type of data structure to make this process a bit fast and less likely to make mistake.
	* Make the string into tuples of letters and their frequences, group the same consecutive letters in the string into one tuple in the list. For example:
		* "ccdee" ---> (c, 2), (d, 1), (e, 2) ---> (1, 2), (2, 1), (2, 3)
		* "aabcc" ---> (a, 2), (b, 1), (c, 2) ---> (1, 2), (2, 1),(2, 3)
* Yeah, it's pretty easy, after this transformation, if both string ends up with the same sequence of tuples, then we know that there exist a set of operations that lead one string to the other.

### More Discussion

* So I went ahead and did it, and then we had a really huge problem, and it's kinda interesting as it's not really clarified in the problem statement.
	* The operations are applied, in a mutable way.
	* Therefore, **if the string has all the characters in the alphebet, then, replacing one of the character in the string to another, will inevitably cause the string to have repeated character** in it, and this is real big prblem.
	* If both strings are saturated, then there is no way to tranform then from one to the other.

* A very intriguing case study:
	* `abcdefghijklmnopqrstuvwxyz` ---> s
	* `bcdefghijklmnopqrstuvwxyzq` ---> t
	* transform is like:
		* a--> b, b--> c, c--> d.... x-->y, y-->z, z-->q
		* Applied them in listed order, one by one.
* What we discussed earlier is not enough, we need more than just tuple frequency list for the problem.
* In fact, the frequences of each consecutive group of characters don't have to match.
	* Take `aaabbb`, `aaaaaa` for example, replacing all `b` in the first string will natrually leed to the second one, but the tuple frequencies pattern of the string is entirely different.

### We Failed and This is Why
* The question is testing us on **Graph Algorithms**.

* Let's make a graph out of it, where each vertex is 26 letters of the alphabet. 

* Assume to string has the same length, else, it's impossible to transform one to the other string. 

* Consider reducing `s` ---> `t`
	* Map the letter `l` to `l'` if the letter is need be transformed in s into a letter in t. 
		* if the letter has multiple edges, then it's impossible to transform `s` to t`t`
		* if the mapping has s cycle in it, then it's impossible

* Constructing the mapper: 
```
Initialize Mapper, 26 length array
for C1, C2 in zip(list(s), list(t)):
	if C1 already has mapped in Mapper:
		return false
	else:
		Mapper[C1] := C2
		
if the range it maps to it's not all the 26 letters, then: true
else: false
```


* Why does the algorithm work
	* If the mapping function is bijective, then a cycle is inevitable. 
	* If one letter attempts to maps to multiple different letter, then the mapping is impossible.
	* if the mapping has a range that is smaller than it's domain and there is no cycle, that mean, we have a temp letter to take as a space to avoid collision while changing the letter in the string, in this case, it's always possible to make the transformation. 
