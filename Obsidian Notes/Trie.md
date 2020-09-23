## Introduction

* The Trie data structure is designed to handle a set of sequences such as sentences and words with a predefined alphebet. 
* This data structure allows for search in real time for a growing prefix from the input. 
* A Trie is a forest/tree, where each node is a symbol from the alphabet, if we take all possible paths from the root node to the leaf while accumulting the symbols, then we obtained all the possible sequences a set. 
	* Or alternatively, we can route to a sub-tree using prefix, and then we will obtain all the sequences in a set such that, they all shared the same prefix.


## What it does: 
* Add a new sequence 
* Delete a certain sequence 
* Given a prefix, returns all the sequence that shares the same prefix in the set of sequences. 


## What is it good for

* It is good for query for all the strings that starts with a certain prefix, and then sorted then acoording to some kind of attributes. 


* See [[Code Vault]], which has implementation of the Trie data structure using hashmap. 
