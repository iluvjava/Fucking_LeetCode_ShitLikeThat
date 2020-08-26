# From Problem Statement

* Arr[I] : [0, 1, 2... len(Arr)] |---> "The Index of That element in the sorted array"

* Inversion: `i < j && arr[i] > arr[j]`

* If you don't know the fact that, the minimum numbr of adjacent swap to reduce the array to a certain permutations
is equal to the number of inversion in the array, then you can't solve this problem .

* If you don't know that, the counting of the inversions in an array is using enhanced merge sort, then
you will not be able to proceed further into the problem.

* Read more here:
  * [Geek For Geek Links](https://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/#:~:text=Inversion%20Count%20for%20an%20array,j%5D%20and%20i%20%3C%20j.)

## Idea: (Enhanced Merge Sort)

* Give 2 sorted array, say: `A:=[a_1, a_2, a_3... a_{n}]`, `B:=[b_1, b_2, b_3... b_{n}]`

  * If there are no inversions, then the desire order for the merged array should be: `[A, B]`.

  * When merging, if there eixsts: `b_i` < `a_j`, then `b_i` creates an inversion for all elements that comes at/after
  `a_j`. Sum that number up for all such `b_i` while merging, then we have the total number of inversion when
  merging the array.

  * Do this recursively, and when merging, take the sum of the total intervsion on the left, right, and the
  inversions obetained when merging 2 arrays.

* Failed Because the recrusive algorith doesn't seem to have the desired speed.


## Take Causions:

* RECURSIVE MERGE SORT IN PYTHON IS NOT FAST ENOUGH TO PAST THE TESTS
  * If you want to do it in python you might need iterative merge sort which will
  reduce the array copying.
* INT DATA TYPE IS NOT ENOUGH TO STORE ALL THE INVERSIONS
  * If you want to do it in java, then you have to use long to keep track of the inversions!
