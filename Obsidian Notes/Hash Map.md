## Sequences Related
Counting number of geometric triplets in a sequence.
	* Problem: [[Count Triplets]]
	* This problem leverage the fact that the **next number on the triplet can be known easily** and we can use 2 dictionaries to keep track of the number of tuples, and the frequencies of the letters to figure out the geo metric subsequences in the original sequence. 
	
* Frequencies Query
	* Keep track of 2 hashmap, which represents a composite mapping.
	* [[Frequencies Queries]]

* Valid String
	* A Valid string is possible if, removing one character will make the remaining string contains letters of the same frequencies in the string
	* [[Sherlock and Valid String]]

* Anagram 
	* A hash map is used to count the frequencies of sorted substring in the array, which is then used to determine all possible pair of substring tha are anagram to each other in the whole string.
	* [[Anagram]]

* Storing all the possible triples from multiple sequences, and query the the number of time each triple is beind shared across the multiple sequences. 
	* [[Analyze User Website Vist Patterns]]
	* Featuring the us of concatenating the string to make the key hashable, which then can be sorted to produce the correct answer to the problem.

### Major Exploits
* HashMap is by far the most widely used exploits in programming. 
* Hashmap used to stores the frequencies of some elements in the sequence, and thengiven the frequencies, tell something about the element with that frequency.
	* [[Sort Characters by Frequency]]
	* [[Analyze User Website Vist Patterns]]
* Used to store the adjacency list of the array, whic is extremely important to the ideas of [[Graph Algorithms]]
