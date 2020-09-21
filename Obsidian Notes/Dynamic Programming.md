
# Dynamic Programming
* Practices include: 
	* Linear Recurrence: [[Max-Array-Sum]]., Hackerrank
	* Edit Distance: [[Abbreviation]], Hackerrank
	* Complex Recursions: [[Candies]], Hacckerrank
	* Trapping Rain Water: [[Trapping-Rain-Water]], Leetcode

## Introduction

* DP is developed during the WWII in the last century, and its central theme is the optimal structure exploitation. 
* A problem is said to have optimal structure if, the the solution of the whole problem contain solutions sub-problems, where sub-problems are problems but with a smaller inputs. 
  * **For example**, consider the weighted interval scheduling problem. An interval scheduling problem gives a list of intervals on a time line, each with a specific weight associated to it, and the task is to look for the set of intervals such that, the weightis maximal and there are no conflicts to the set of intervals.
  * given the current optimal solution and soluitons to all the sub problems, and consider any additional time interval being added, such that: the new added interval's finishing time is beyond all the current interval. 
  * Assumes that the array is sorted by the finishing time of the intervals in the set, name the set of intervals `A`
  * Assumes that, for all sub problems, `A[:I]` where `0 < I <= len(A)`, we have the optimal solutions.
  * Assume a new interval with finishing time that is beyond all elements in `A` is added, then the new solution is constructed based on all previous solution:
	  * Name the new added interval `I_{n+1}`, find starting time, and look for the interval in `A` such that it doesn't have a direct conflict, say that one is `J` in `A`, then we have recursion that can construct new optimal solution that includes the new interval: 
	  * `Opt[I + 1] = min(Opt[J] + W[I + 1], Opt[I])`, where `W[I]` is the weight of the new interval. 
  

## The Approach
* Recursion, but brute forces. 
* If Dynamic Programming is applicable, then there will be repeated subproblems being solved, which can be stored using a datastructure to save run-time for the algorithm. 
	* This is Memoization
	* Improve the recursion either with a bottom up approach, or with a iterative solution to the recursion to avoid stackoverflow. 
* Most Commonly use data structure is: "Hash Map"


## Noble Applications of Dynamic Programming
 1. Edit Distance of String
 2. Computing Hidden Markov Chain
 3. Longest Common Subsequence
 4. Largest Empty Square
 5. TSP: Kelp Harp Algorithm
 6. Bellman Ford Sortest Path: Edge Relaxation


## Divide and Conquer
* Divided and Conquer is a special case of Dynamic programming where, we only need k, optimal soluitons, all with very similar sizes to reconstruct the solution to a larger problem. 
* **Noble Applications**: 
	* Merge Sort
	*  Fast Fourier Transform
	*  Strassen's Matrix Multiplication
	*  Karatsuba Algorithm
	*  Convex Hull
	*  Voronoi Diagram Generation

