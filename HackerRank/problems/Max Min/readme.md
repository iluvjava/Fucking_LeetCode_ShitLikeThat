# Problem Statement

* Given an array of integers, find the subset of integers with K elements in it, call it `subarr`, such that
the value `max(subarr) - min(subarr)` is minimized.

* If k = 2, them the probem reduced to `./Minimum Absolute Difference in an array`

* Statement (1):
  * For all possible solution to the problem, they must be a continous array with length k in the original array.

  * Assume that this is not the case, then choose the elements that are furthrest away from the center (The average of
  all the elements in the subarray) and then swap it with that element in the array, then, the maximum unfairness will
  be minimized.

  * Therefore, all the subset that are not a continuous sub-array in the sorted array are not in the solution set.

## Algorithm using statement (1)

* Sort the integers in the array.

* For all possible continous sub array with a length k, get the `max(subarr) - min(subarr)` and then get the minmum out
of all of them.

* This algorithm failed because direct implementation using array didn't give good run-timne for the testcases. 

* It also failed one of the testcase for some inexplicable reasons.

## Optimizing the solution

* Using the Python heapify for arrays.
  * this should be as good as other things.
  * Use a min and max structure for the heapified array.
* Using the priority queue data structure like in java.
  

## One extra thing

* This code challenge tells us that, we should get an implementation that uses the
heapq in python to make a heap datastructure for coding problems like these.  

* The heapq in python doesn't support removal of any elements that is already in the heap. 
  * Which is a big bummer.
  