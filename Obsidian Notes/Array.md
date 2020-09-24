## Array is a very Fundemental Data Structure

* An array can be interpreted as a special hash map where the key is the intergers, within a certain range, and the element is the reference to the variable.

### The idea of Inversions of Elements
* [[Count Inversions]], Using Enhanced Merge Sort
* [[New-Year-Chaos]]
	* 2 Elements, a, b are forming an inversion if and only if. 
		* Assuming `a`, `b` are at `I`, `J` of the array, and yet, `a < b` but `I > J`, and they are out or ascending orders. 
	* The idea can be generalized by defining a **unique permutations** out of the given set of elements. 
		* Consider the arrray `Arr` to be the array, and consider `Per` to be the an unique permutations of elements in `Arr`, then an inversion can be formed between `Arr` and `Per`. 
		* Let's assume that, `Rra[Arr[I]] = I`, so that, `Rra` is the reverse mapping of elements in `Arr`. 
			* Take 2 indices of `Arr`, WLOG, assume `I`, `J` where `I < J`. 
			* Then `Arr[I]`, `Arr[J]` forms an inversion if: `Arr[I] > Arr[J]`. 

* **Extremely Useful Facts**: 
	* Bubble Sort uses adjacent swaps to reduce the permuations to a sorted one, and the swaps involved in bubble sort is the same as the number of inversions in the array.
	* The number of inverions in the array is the same as the bumber of adjacent swapps that is needed to map the current permutations to the sorted permutation of the array.

### Minimum Swaps Needed to Sort the Array

* Which is the same as the number of swapps performed during the selection sort. 
* And reducing it to a graph problem will help us to find the minimum swaps needed to reduce it in linear time. 
	* [[Minimum Swaps 2]]
* A lot of things that make use of array to design efficient algorithms involve the cloever use of the indices, the mapping nature of the array, and the use of the partitioning the array, sometimes mixed with dynamic programming.

### Dealing with Intervals on the array 
* [[Array-Manipulations]]
* Problem makes each intervals to be associated with a certain values which are added to the whole interval on the array. 
* The problem asks us to keep track of that and then return the maximal value across the whole array after all of them. 
	* The solution behind it is to sort the interval, left boundary and the right boundary, and then use a hash map to model the intervals and the actions of  (Adding) filling in the intervals on the array with a certain number. 

## Noticable Exploits of Array
### An In Place Array Rotation Algorithm
* [link](https://www.geeksforgeeks.org/array-rotation/); the Juggling algorithm
* Which is also mentioned in [[Hacckerrank_General_Guide]]
* Here is a domostration.
	* Given an array of length 6, rotate elements left by 2, in place.
	* `[1, 2 | 3, 4 | 5, 6]` partition the array into segments of 2.
	* `[3, 2 | 5, 4 | 1, 6]` rotate for all first elements in each partition
	* `[3, 4 | 5, 6 | 1, 2]` rotate for all second element in each partition
	* A rotation of 2 has achieved.
	* if applied 2 rotations on each partition, then a rotation of 4 will be achieve. 
* Consider a much general case where, the length of the array is `n` and the amount of total rotation needed is `d`.
	* partition the array using `k = GCD(d, n)` hence, `n` is divisible by `k`
	* determine the amount of rotation in each partition by the quantity `d/k`, which must be an integer.
	* Rotate `d/k` amount for each element in partition, from partitions to partitions.
* A similar practice problem that partition the array and make use of dynamic programming too, see [[Trapping-Rain-Water]].