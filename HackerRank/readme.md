# What is this?

* A Summarization of Ideas for Coding Challenges in General.

* Coding challenges from companies are design to throw people who are not preapred out of balance, and then filter

them out. This can be seem easily through the coding challanges they send to people.

* If this is really their strategy, then this repo provides the counter strategies.

## Arrays Related

### Jungling Algorithm

* Used when rotating an array without extra memory
[Link](https://www.geeksforgeeks.org/array-rotation/)

* <img src="Jungling Algorithm.png" width="500px"/>

* Enhance Merge Sort as a way of counting inversions
  * The number of inversion is directly related to the number of adjacent swapps
  going from a sorted list to an unsorted list.

### Intervals

* When the problem involves doing something on some interval defined by indices (I, J) on the array, we
might need to consider:

  * Using Map to model it and use some sorting to traverse all the intervals in order.

  * Problem involved: `./problems/Array Manipulations`

### Inversion (Related to Sorting)

* The # of Inversions in the array is from Enhanced Merged Sort.

* The # of Inversions equals to the minimum number of adjacent swapping for to sort the elements. (Or reducing it
to a predefined permutations)

* A inversion counting algorithm is implemented in: `problems/New Year Chaos`, in **Java**.

### Minimum Swaps (Related to Sorting)

* The # of minimum swapp to reduce the array to a certain permutation (sorted order) is reduced to a cycle detection

problem. See `./problems/Minimum Swaps 2` for more information.

  * Def: Array: a list of integers where `Arr[I]` the value represents the desired index of element `Arr[I]`.

  * Then, a digraph by linking the `I` to `Arr[I]` (Mapps the element's actualy index to the index where it SHOULD be in

  ) gives a digraph with only simple cycles.

  * The sum for all cycle's length - 1 gives the total number of swaps needed to reduced the array to a pre-defined
  permutations.

### Frequencies and Mapping

* Array can be used as a map that maps the indices of an element to any value correlates to the index.

* An array implemented median seeker in python is provided in `./problems/Fraudulant Activity Notifications`

## Set, Map Related

### Anagram

* An anagram of substring is defined to be the substring of a string that are
permutations of each other.

* All substring has a unique permutations to it, putting them into a set
structure will create basis for comparison.

### Frequencies Tables

* It is another widely used idea in Set, and Map related coding challenges, arises when we need to keep track of the

freuqncies of each element.

* Learn how to use them for a set of element involvng repeatitions.

### Composite Mapping

* Know how to design a mapping mechanism via composite mapping, see `./problems/Frequencies Queries`.

* Keeping a mapping of M: (A) |---> (B) |---> (C) while iterating through some data input stream.
  * e.g: A is word in a string, B is the frequencies of the word appeared in the string, C is the number of words with
  that frequencies B in the string.

### Discontinous Subsequences

* Discontinous Subsequences: full sequence: {a_1, a_2, a_3... a_n}, Subsequences: {a_i_1, a_i_2, a_i_3... } where for all

indices `i_k`, `1 <= k <= n`, `i_k < i_{k - 1}`.

  * e.g: Full sequencies {a_1, a_2, a_3, a_4, a_5... , a_n}

  * subsequence: {a_1, a_5, a_7, a_8... a_{n - 3}}

* Using a map to count the number of subsequences satisfying a certain conditions:

  * Constraints 1: Give any e_n in the subsequence, e_{n + 1} can be easily determine.

    * e.g: Geometric, Atrithmetic, letters in alphabetical order.

  * Constraints 2: All the subsequence under the search space must be with the same length.

* Usage is demonstrated in  `./problems/count-triplets 1`

* Traversing the array in reverse order, using a map to keep track of the number of tuples and the frequencies for each

single elements already appeared while traversing the array.

* Using those information to get the total number of triplets sub-sequences that are involved in the array.

## Dynamic Programming Related

### In General

* If the problem is discussed in class and it has the common patterns on the recrusion and we already have a
algorithm for, eg. Longest Common Substring
  * Applied the algorithm by copying the recursion table and then write codes that solve the problem.

* If that is not the case and the problem seem unconventional, use the BIG GUN:
  * Investigate recursive structure.
  * Write a simple recursion and then solve it on small instances to verify that it's correct.
  * Use Memeorization.
  * Stackify it if stack over flow problem occured.

### Prefix Sum

* Accumulating the partial sum for a given 2d or 1d array.