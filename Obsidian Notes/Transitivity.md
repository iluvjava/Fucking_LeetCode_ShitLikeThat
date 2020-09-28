# Intro

* A mathematical relation is said to be transitive, it means the following. 
	* Let $R$ be an relation on $A\times A$
	* Then the relation is transitive if: 
		* $(a, b)\in R \wedge (b, c) \in R \implies (a, c)\in R$


### Examples
* Loading


### A Problem
* [[Median of Two Sorted Arrays]]

* Inputs: Given 2 sorted array with different length, find the median of 2 of the array when sorted together. 
	* The expected complexity should be: $O(\log{(N + M)})$ where $N$ and $M$ are sizes of the array. 
* Intution
	* It's like a binary search, but it's on 2 arrays instead of one. 

### Discussion 
* **For Simplicity **
	* Assume that the array has the same length, denotes as `N`
	* Assume that `N` is  odd. 
* Notations: 
	* Denotes 2 ofthe arrays as `arr1` and `arr2`
* Given $M1, M2$ as the median of `arr1` and `arr2`, and let the set $S$ denotes all the element from both array. 
	* The number of elements larger than `M1` is $\lfloor N/2 \rfloor$. 
	* The number of elements less than `M2` is $\lfloor N/2 \rfloor$. 
* Let's assume that the $M1, M2$ have index $I$ on both arrays.
* Now let's discuss some of the possible relations between `M1` and `M2`. 
	* $M1 < M2$, then median of both array, say $M3$ has the following possibility: 
		* $M3 = arr1[J]$  where $J > I$
		* $M3 = arr2[J]$ where $J < I$
		* This is true because $M1 < M3 < M2$, if this is not the case, then there are not enough numbers of integers in the array that can be larger than $M3$, since the total number of both array has $2N$ integers, and $M3 < M1$ or $M3 > M2$ will implies that, there are $\lfloor N/2 \rfloor$ number less than $M3$ or there are $\lfloor N/2 \rfloor$ numbers larger than $M3$, hence in this case $M3$ must be in between $M1, M2$, and this will imply its index in `arr1` and `arr2`. 
		* This is true by transitivity of the integer inequality. 
	* $M2 < M1$, then the median of both array can lie in the following region:
		* $M3 < I$ in `arr2` or $M3 > I$ in `arr1`. 