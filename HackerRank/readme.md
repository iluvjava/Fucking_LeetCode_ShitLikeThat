# What is this

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

* The problem presented from the copanies will have fancy names and long description to mask what the problem it
is exactly, preventing the candidtate from reaching to google if the candidate cannot phrase the problem correctly
and don't know how to describe the problem.

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

## Stack and Queue Related

* The Stack data strcuture is widely use for:
  * Reversing the order of element.
  * Verifying the balance of rackets.
  * Parsing expression tree.
  * Reading the traversal of tree nodes.

* The stack data structure have weird usage for:
  * Identifying the nearest element that are immediate smaller/larger on the left/right for the element in that array.
    * See more at : `.\problems\Largest Rectangle`
    * `.\problems\Min Max Riddle`
    * This is an extremely new idea for me.
  * The idea is to keep a monotonic increasing/decreasing stack such that, we can figure out the immediate
  elements that are immediate larger/smaller on the left/right side than the current element in a O(n) time.
  * This features of the stack is tested implicitly for a lot of the programming challenges.

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

* Identifying Dynamic Programming Problem
  * A dynamic programming problem experiences the optimal structure:
    * The optimal solution of a problem can be constructucted from the optimal solutions
    of the sub-problems.
    * A greedy algorithms can be solved with dynamic programming

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

* Foreach(I: The I th interval in the list of intervals):

  * find J: The latest interval such that it doesn't have any conflict with the I th interval.

## Greedy Algorithm Related

* Greedy algorithm is not hard, the hard part is identifying that, a greedy algorithm works for a certain problem,
because, for most of the optimization problem outthere, it always never works. So we must prove it to make sure that
it works for that given algorithm. Here are some famous examples of problems that can be solved Greedily:

* MST.
* Shortest path without negative edge weights.
* Squeeze Min/Max number of intervals in a certain time frame.
* Minimum absolute minmax for a window size for an array.
  * a lot of them in the greedy section of Hackerrank contains the idea of sorting elements.

### Reasoning with Greedy

* The reasons why greedy algorith works is very complicated and we have to use the idea of Matroid to prove that.

* But in general, it can be prove inductively by showing that, at each step, a greedy choice built up previous
optimal solution will keep its global optimality.

* If, it's hard to prove that greedy algorithm works, then we need to bet on counter examples that break it.
  * When looking for a counter example for something, tries to use different permutations for the greedy choices, and
  if the solution differs, then greedy algorithm cannot produce the optimal solution for the problem.


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

### BFS

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

### DFS

* DFS tree.
  * Ancestors on the branches, no crossing between different branches.
* Connected Components.
* Topological Sort.

```python
def dfs(StartV):
    Stack := Stack
    Visited := Set
    Visited := add "StartV" to Visited
    while Stack is not empty:
      V = stack.pop()
      foreach W as neighbours of V:
        Visited.add(W)
        Stack.add(W)
    return Visited
```

* Or we can have a recursive version of the same thing:

```
def dfs(StartV, Visited=None):
    Initialize Visited as a set if it haven't.
    Visited.add(StartV)
    for W as neibours of Vstart:
      dfs(W, Visited)
```

### Topological Sort (Just something I love)

* There are 3 algorithms for doing Topological Sort, with different run-time.
* Preconditions of the algorithm:Input is a Directed Acyclic Graph

* Using Priority Queue.
  * Rank all the vertices with their indegree.
  * Pick vertices from the top, and then decrement it's neghbours indegree and update them
  in the priority queue. Put that vertex into the another stack, storing the topological sequences, repeat
  this process until the priority queue becomes empty.
    * if at anypoint, the vertex at the front of the priority queue has an indegree of 1 or more, then
    the graph contains cycles.
  * This approaches highly depends on the implementation of the "Priority Queue"

* Using a "Indegree storage auxlilary data structure"
  * Let L[V: vertex in the graph] stores the indegree for each of the vertices.
  * Let Q be the stack that stores the list of vertices in topolotical order.
  * Initialize an collection, Arr, containing all the vertices that has an indegree of 0
    * while(Arr is not empty)
      * Take V out of Arr add it to Q
      * foreach(Vertex W as neighbours of V)
        * L[W]--
        * If L[W] == 0:
          * Add W to Arr

* Using the DFS algorithm.
  * This modifies the DFS algorithm and suit it for the Topolotical sort algorithm.
  * While traversing in DFS order, at the back-tracking process, add the nodes in reverse order then we have the
  topolotical ordering with respect to that vertex in the graph.
  * A modified verson of this one can be used to construct some kinda of Acyclic Graph from any simple digraph.

## Basic facts

* The numeber of edges and connected components. (|V| - 1) to be the minimum.

