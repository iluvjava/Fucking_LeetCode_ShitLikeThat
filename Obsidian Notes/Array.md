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

### Dealing with Intervals on the array 
* [[Array-Manipulations]]
* Problem makes each intervals to be associated with a certain values which are added to the whole interval on the array. 
* The problem asks us to keep track of that and then return the maximal value across the whole array after all of them. 
	* The solution behind it is to sort the interval, left boundary and the right boundary, and then use a hash map to model the intervals and the actions of  (Adding) filling in the intervals on the array with a certain number. 
	* 
 