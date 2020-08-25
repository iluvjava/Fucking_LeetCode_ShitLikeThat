## Information From Problem Statement

* Assuming you have read the problem statement. <a href="https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting">here</a>

* The problem gives a window size of `d` on the array, and it slides the window across the array, keeping track of the 
median of all numbers that are in the window.

* If any incoming number to the window is 2 times larger than the median inside, then there we need to increment 
the number of "fraudulent activities".

* Obseve that, all possible numbers in the array is very small, and its stated as between 0 and 200, inclusive.
  * This is a big big hint that, the usage of heap, dequeue, or linked list and sorting might not be desirable. 

## Idea 1
* Use an array of fixed size to keep track of the median, this requires some really big brain solution. 
* assume an array to keep tracks of all the counts of the numbers. 
  * The frequencies of the element E, is arr[E]
  * Then, the median is at the slot when the sum of the frequencies is n//2, n is the all the number of elements.
  * We need a data strcuture to keep track of this number. 

### The Median Keeper
* Specify all the possible integer values for a given stream of inputs, WLOG, assume 1 <= I <= M
* Assume that, there exists a pointer that points to the median element. 
  * Say the median is 50, and 50 appeared 2 times and the n//2 th element is the last appearance of 50, then the point 
  should be a tuple, P:(50, 2), and it means that, it's pointing at the second element at the index 50 of the array. 
  * Question: How to update the data structure while elements adds in and move out? 
* Add(E), Complexity O(nM): 
  * Increament the count for element E, update the number the pointer is pointing at. 
  * Assuming P:(I, J)
    * arr[E]++ Increment the frequency for the element first.
    * If E == I:
      * Update J if the new array size is even.
    * If E < I:
      * Update J if the new array size is even. 
        * Decreement J, if J <= 0, search the left array and find the first element which frequency is non zero.
        Points to the last element of the value. find K such that arr[K] >= 1 update P as P(K, arr[K]). 
    * If E > I:
      * Similar Story to the above case, it's left to the reader to ponder this. 
* GetMedian(E):
  * Find the pointer and the next number right after the number the pointer is point at.
  * The the average of them if the total number of elements are even. 
  * Else just return the number the point is pointing at. (The index of the array that the pointer is pointing at. )
* Remove(E):
  * Decrement the count for E, move the pointer.   
* Corollary: 
  * This data structure can be modified for other purposes, for example, fuzzy median locator. (That is if we only 
  care about the approximate range of the median of an inputs stream)

## Idea 2
* Use a min, max heap to keep track of the median, and the heap better supports removal of elements. 

