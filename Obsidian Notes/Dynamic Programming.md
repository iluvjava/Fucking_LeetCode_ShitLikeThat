
# Dynamic Programming
* Practices include: 
	* Linear Recurrence: [[Max-Array-Sum]]., Hackerrank
	* Edit Distance: [[Abbreviation]], Hackerrank
	* Complex Linear Recursions: [[Candies]], Hacckerrank
	* Trapping Rain Water: [[Trapping-Rain-Water]], Leetcode
	* Edit Distance: [[Edit Distance]], Leetcode
	* Prefix Sum of 2d/1d Array, ???
	* Longest Common Substring Between 2 Strings: [[Common Child]]
	* Maximal of all Continous Subarray: [[Sliding Window Maximum]]
	* Find Maximal sum of Continuous sub array: [[Maximal Subarray]]
	* Finding the shortest contiguous substring containing a given sequence: [[Minimum Window Subsequence]]

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

## Notable Exploits

* Prefix sum, while iterating through the array, 1d, or 2d, stores the partial sum of the array in another array. 
* Longest Common Substring: 
	* define `T[I, J]:= The longest common substring between the substring a[:I + 1] and b[:J + 1]`, then we can have the following recurrcences:
	* If the current characters for both points `I`, `J` points to the same character in both string, then: 
		* `T[I + 1, J + 1]:= T[I, J] + 1`
	* Else, if the character at those 2 pointers in the string are not pointing at the same character, then: 
		* `T[I + 1, J + 1] := max(T[I - 1, J], T[I, J - 1])`
		* It can be extended to incorperate more operations about the string, this is exploited by the following practices problems: 
			* [[Common Child]]
			* [[Edit Distance]]
	* Maximal of the partial array
		* This is very similar to the prefix sum exploit, where we stored the following about our array.
		* Define `T[I]:= max(Arr[:I+1])` 
		* `T[I + 1] = max(T[I], Arr[I + 1])`
		* Then, then stored the array can be used to speed up some of the computations, this is the exploit in the following practices problems: 
			* [[Trapping-Rain-Water]]
			* [[Sliding Window Maximum]]
  

## The Approach
* Recursion, but brute forces. 
* If Dynamic Programming is applicable, then there will be repeated subproblems being solved, which can be stored using a datastructure to save run-time for the algorithm. 
	* This is Memoization
	* Improve the recursion either with a bottom up approach, or with a iterative solution to the recursion to avoid stackoverflow. 
* Most Commonly use data structure is: "Hash Map"
* [[Stackify Recursive Functions]]


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

## Some Involved Examples
* Given a set of items with profits and weight, and a knapsack with a capacity, we want to maximize the profits without exceeding the weight constraint.
* Knapsack but all items has the same value, by which I mean the weights and profits equal to each other.
* Consider a set of items where we want to take as many items as possible within a weight constraint.
* List of variables:
	* Denotes: `T[I, W]:= "A binary value representing whether there exists a subset of arr[:I + 1] such that it sums up to W."`
	* Denotes: `arr` to be the list of the weights for each items, assume weights are integers.
	* Denotes: `Budget` to be the total amount of capacity allowed for the knapsack.
* For the `I + 1` items, we have the choice of adding it in, or not adding it in.
	* `T[I + 1, W]:= T[I, W - arr[I]]` if we add it in.
	* `T[I + 1, W]:= T[I, W]` if we don't add it in.
	* `T[I + 1, W]:= (W == arr[I + 1])` an edge case (Should be eliminated by handling the base cases)
* Therefore the recurrences can be simply put as: 
	* `T[I + 1, W]:= T[I, W] || T[I, W - arr[I]]`
* Base cases: 
	* When there are no items to choose from, it automatically sums up to a weight of zero. Otherwiese false.
		* `T[-1, W]:= (W == 0)`
	* In fact, the empty set will always has a weight of 0, it will eliminate case 3 of the recurrence.
		* `T[I, 0]:= True for all I`
* Further Optimizing the memory:
	* Notice that only the `I - 1` is used, therefore, we can only keep the last row to produce the next row (assuming `T` is a table, where different I lays on the columns and different `W` sweeps across the rows)