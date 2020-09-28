# Problem Statement

* Input: 2 arrays of integers. 
* output: 
  * The maximal length of the **none empty, cotiguous sub-array** such that, for any 2 given elements in the array, their 
  differences in absolute value will be less than the given limit. 
* Constraint:
	* The array of the numbers are always positive integers. 

* This problem is relavent to GOOGLE


## Brainstroming
* Variables:
	* `arr`: The array of positive integers, from the intpus of the problem. 
* How to handle the absolute value thing.... 
	* `abs(for E in arr[I: J + 1]) = max(arr[:I + 1]) - min(arr[J: ])`
* It's relavent to the maximal and minal elements in the subarray. 
	* `MaxL[I]= max(E for E in arr[0: I + 1])`
	* What can we say about `max(arr[I: J + 1])`? 
	* if `MaxL[J] >= MaxL[I]`, then `max(arr[I: J + 1]) = MaxL[J]`
	* else: We don't know for sure.

* If we are given the fact that, all the numbers are positive integers, how could that be an exploit for his problem? 
	* Don't know yet. 

* Can we keep track of the maximal and minimal elements in the contiguos sub-array while iterating through the array? 
	* `Max[I, J] := max(arr[I: J + 1])`
	* `Min[I, J] := min(arr[I: J + 1])`
	* Recurrence: 
		* `Max[I, J] = max(Max[I, J - 1], arr[J])`
		* minimal is the same
		* Construction O(N^2)

* With this, we can now iterator through all the windows and then find the maximal length such that the difference between the minimal and  the maximal is within the given limit. 


### Problem
* Some of the testcases have huge inputs, we need a O(N) solution. 

* This is not a test on dynamic programming 


### More Brainstorming

* Use a sorted Tree to keep track of the minimum and maximum while sliding through the array. 
* The best way to solve this problem is to use a sorted multi-set, in hope of improve some speed when there are a lot of repeating elements in the array. 

* Check the current folder for the Java solution using a customized Ordered Multi-set to handle the problem. 