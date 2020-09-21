## Strings are Sequences of Symbols

* Sometimes, the problem as as to manipuate or determin something about a sequences of symbols, and this is what we are interested in. 



* Counting the number of special string in a sequence. 
	* This probelm is concered with counting string with even length such that, all the characters are the same OR string of odd length where, the middle character is different, while all other characters are the same. 
	* [[Special String Again]]

* Counting the number of substrings in a string that are anagram to each other
	* This problem features a clever usage of the hashmap and sorting the characters in a string, see this problem: [[Anagram]]

* Edit Distance
	* Given a set of operations applied to the sequence of symbols, each might be associated with a cost: 
		* Figure out the minimum operations needed to reduce one string to another using the given set of operations.
		* [[Edit Distance]]
		* [[Abbreviation]]
		* [[Common Child]]
	
### Sequences of Integers

* This is a special case of sequences of symbols, it's special because numbers support more operations than just symbols and it has more specific features to it. 
	* This is especially true when it gets combined with arrays and indices of the array.