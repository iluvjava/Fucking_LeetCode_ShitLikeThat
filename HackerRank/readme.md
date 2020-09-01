# What is this?

* A Summarization of Ideas for Coding Challenges in General (for Hackrrank coding challenges).

* Coding challenges from companies are design to throw people who are not preapred out of balance, and then filter

them out. This can be seem easily through the coding challanges they send to people.

* If this is really their strategy, then this repo provides the counter strategies.

## Things at front

* There are something to keep in mind when solving interview problems in general.

* **The 80% rule**:
  * only start coding the solution when you know above 80% about the problem you are solving at hands.

* If constraints are **explicit given**, please think about it and its implications.
j
* Read the conditions of the problem carefully and make use of all relavent information.
  * unlike solving problem in the real worlds, the relavent information in the coding challanges are always
  useful information for producing the correct/optimal solution for the problem.

* Start coding NOW!

## Common Good Strategies for Coding Problem

* Read the problem carefully, and if no ideas pop up immediately, skip and do the next one to save time.

* When during interview, you have to communicate with the interviewers to get what they are trying to do and do the
problem under their guides. This is a process of communications.

* **Dimentionality Reduction**:
  * Reduce the dimension of the problem too see if it gets into an easier problem, sometimes, the subroutine for
  solving the problem is in the sobroutine.

* **Spacial Case Inspiration**

  * Consider an special case of the problem, especially consider the problem for an easier instance. If that problem
  can be solved, then there is a "Partial solution" of the full solution hidden in how the special cased is solved.

* **Base Cases**
  * This one is escpecially important because a lot of the recursive backtracking/Dynamic programming solution comes
  down to a good analysis of the base cases, and the is also the place where a lot of problems are having a **good
  amount of diversity**.


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

### Minimum Swaps (Related to Sorting, not necessarily adjacent swapping)

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
algorithm for, eg. Longest Common Substring, Weighted Interval, KnapSack, Prefix Sum, Isotonic Regression.

  * Applied the algorithm by copying the recursion table and then write codes that solve the problem.

* If that is not the case and the problem seem unconventional, use the BIG GUN:

  * Investigate recursive structure.
  * Write a simple recursion and then solve it on small instances to verify that it's correct.
  * Use Memoization.
  * Stackify it if stack over flow problem occured.
  * Tablularized if the patterns of recursion can be easily put into forloops and such.

### Stackfication of With Memerization of DP

* The Recursion Stack Stores all the parameters needed for the algorithm, (or some kind of identifier that helps with
looking up the parameters in another data structure)

* Call the Memerization table T.

* If the parameter given is already in the table, then remove the parameter and `continue` back to while loop, else:

  * if Branch, then check if the parameters is in the Memorization or not, if it is, then skip the branching process.

  * prepare the branching process first, for each of the sub problems, add the needed parameters for the sub-problem
  and `continue` back to the loop.

  * if all the branching sub-problem has been solved, merge results using the table T.

  * store the new results to table T, pop that parameter because the problem has been solved.

### Prefix Sum (Common Patterns)

* Accumulating the partial sum for a given 2d or 1d array.
  * The 1d is kinda trivial
* Recurrence Structure:
  * T[I, J] := "The sum of the sub-array on the top right corner, and the bottom right corner
  locates at [I, J] inclusive"

  * T[I, J] = T[I - 1, J] + T[I, J - 1] + T[I - 1, J - 1]

  * Base Cases:
    * T[I < 0, J < 0] = 0; If you want to sum them up, then you better start summing up from zero.
    * And there are other ways.
      * T[I = 0, for all J] = arr[0][J], T[for all I, J = 0] = arr[I][0], T[0, 0] = T[I, J]
      * This one won't support empty array anymore, but it's more legit because it follows the
      philosophy that, a sum has to start with something.

### Longest Common Sub-String

* Looking for the longest common discontinous substring between any 2 given string uses dynamic programming and it's
related to edit distance of 2 strings. Say the 2 strings are denoted as `A`, `B`.

* For the `I` th element in the string a and the `J` th element in string b, there are the several cases:
  * If `A[I] == B[J]`, then that letter has to be in the longest common substring.

* Recurrence:
  * T[I, J]:= The length of the longest common substring between the the prefix of `A[:I + 1]` and `B[:J + 1]`.
  * Then:
    * T[I, J] := Max(T[I - 1, J], T[I, J - 1]) if A[I] != B[J]
    * T[I, J] := T[I - 1, J - 1] + 1 if A[I] == B[J]
  * Base Cases:
    * The longest common substring where one of the string is empty, is 0


### Edit Distance

* Edit distance is defined to be the number of INSERT, REPLACE, DELETE that edit from one string to the other string. 

* Say 2 of the string that we are interested is: `A`, `B`.



### Weighted Inverval Scheduling

## Greedy Algorithm Related

## Graph Algorithm Related

* In general:
  * Don't expect things that are too hard like Network flow, Negative Cycles, Clique delection or Independent sets.
  * Expect simple stuff. I don't think they will even touch on negative weight edges.
  * Careful what assumption to make, espcailly about the connectivity of the graph, can't assume anything if
  it's not explicitly given in the problem.

## Triangle Inequalities

  * Use this to simplify and optimize the runtime of some algorithms, see (./HackerRank/Find Nearest Clone) for
  example.
  * Use that fact and pair it with algorithm on shortest distances.

## Think Inductively and come up with good examples.

* This is very important when doing graph coding challenges.

### BFS:

* BFS tree.
  * Levels.
  * Edges doesn't cross more than 2 levels on the tree.
* Unweighted Directed/Undirected simple graph.
* Expanding like a spider when searching.

* The vertex it visted.
* The edge distance to the root.
* The size of the connected components associated with a vertex.
* Always remember SINGLETON!

```python
def dfs(v, adjList):
  Q = [v]
  Visited = {}
  while len(Q) != 0:
    U = Q.pop(0)  # change here to make DFS
    for W in adjList[U]:
      if W not in Visited:
        Visited.add(W)
        Q.add(W)
  else:
    Return Visited
  return set([v])  # singleton.
```

### DFS:

* DFS tree.
  * Ancestors on the branches, no crossing between different branches.
* Connected Components.


## Basic facts

* The numeber of edges and connected components. (|V| - 1) to be the minimum.

