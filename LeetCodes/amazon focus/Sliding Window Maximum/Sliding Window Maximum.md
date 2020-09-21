# Problem Statement

* Open a sliding window with size k on the array,  we slides it through the array and keep track
of the maximum element in the window, and then we want to know what maximum value all the windows
that we can slide through the array.

* It's asking us to return the maximal of the K-sliding whindow as it swept through the array. 

* Example:

```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3 ,5 ,5 ,6, 7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

## Solution Using Sorted Data Structure

* Use a tree map in java to keep track of the maximal element as we opens up an window and slides
it through the array and keeping track of the maximal element as we slides the k-sized window
across the array.

```
Initialize: Arr, the input array.
Initialize: TreeMap: T, comtaining the first k elements in the array.
RunningMax = T.max()
for I := from k + 1 to len(Arr) - 1:
    T.remove(T.max())
    T.add(Arr[I])
    RunningMax = max(RunningMax, T.max())

return RunningMax
```

## Solution using Dynamic Programming

* Partition the array into continous block of k, except for the last one, which might be a bit
shorter than k.

* Let's talk about the recurrences.

  * Divides the array into `M` partitions, where the first `M-1` partitions are of size k, except for the last one,
  which depends on the modules of `N%k`, where `N` is the size of the array.

  * Locates the index `I, J` on the array, where the width of the window is k, then we know that, there are 2 possible
  casses

    * The window spans across the same partition on the array

      * Let `k` be the index that is pointing to the first element on the second partion, then the following is true:

      * `Maximal of the window = max(max of partial on arr[I:k], max of partial on arr[k:J])`, delete the definion of
      k and revert it back to the size of the open sliding window.

      * Notice that, we had made use of the partial maximal of arrays, but for each `k` size partitions of the array.

    * The window spans across 2 different partitions on the array.
      * Then we just the use the whole sum of the partition, which is equal to the maximal elements too. 

* The idea under exploitation is: "Maximum/Mimum value of a partial, continous subarray. "
  * Partition the array into k parts, except for the last partition, and if `len(arr)%k != 0`, the last partition
  is gonna be a little bit shorter.

  * for each of the sub partition, construct the partial maximal DP structure for the problem.

