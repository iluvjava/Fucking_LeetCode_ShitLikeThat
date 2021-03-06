# Problem Statement

* [link](https://www.hackerrank.com/challenges/min-max-riddle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues)

* For each window size among all possible window sizes, find the maximum of the minimum.
  * The mminimum of a window size on an array is the the minimum of the elements for the window while it slides
  through the array.

## Idea 0 (The brute force)

* Make a window of each size, sweep it through the array and get the minimum for the window size.

## Idea 1 (Not working)

* Are we using priority queue for this problem?

* That means we are going to use it a lot of time, for different window sizes and that can be pretty slow.

* Yeah, this is not working well, I don't think it has enough efficiency for the problem.

## Idea 2 (From Geek for Geek)

* So this problem have the same exploit as problem `..\Largest Rectangle`, but it uses the idea of it, not even
using its subroutine.

* It uses the stack to look for the nearest, smaller element for each of the elements in the array.

* And using the information about the nearest smallest element, we can construct the minimum for each window sizes.

* [Geek link](https://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/)

### Reasoning

* For each of the element `arr[I]` in the array, we find the nearest smaller element on its left and right, say
`arr[K] < arr[I], arr[J] < arr[I]` where, `K > J`

* Then, we know that, for all window sizes, s such that `1 <= K <= K - J`, the element `arr[I]` is going to be the
minimum of those window sizes.

* To look for, 2 arrays of indices that denotes the immediate smaller element on the left and right of the element
at `I` we use the similar stack strategies described in `..\Largest Reactangle`


* Then, use those 2 array to get the window size for each of the element, so we have a map:
`index of the element` |---> `size of the window that contain that element such that the minimum is that element`

* Then use that, for each window size, we iterate through the array and update them.

### Let's try it out by hands and see what we can learn

* Let the input of the problem be:
  * `[1, 2, 3, 5, 1, 13, 3]`
* For each element in the array, find the immediate left, right smaller elements.
  * Right immediate smaller: `[None, 4, 4, 4, None, 6, None]`
    * Where none denotes that, the element is out of the index, and it's like far far beyond the
    right side of the array.
  * Left immediate smaller: `[None, 0, 1, 2, None, 4, 4]`

  * For immediate element that are on the left side that are smaller, replace `None` with -1 and
  for the right side, use `len(arr)`, which is `7`, then we get the following 2 arrays:
  * `[7, 4, 4, 4, 7, 6, 7]`, `[-1, 0, 1, 2, -1, 4, 4]`
  * Using the arrays, we an computer the window size such that, the minimum is that number.
  * Formula: `R - L - 1`
    * `[7, 3, 3, 1, 7, 1, 2]`
* Using the data we obtained from the previous part, we will be able to obtained the soulution.
  * create map with array, where the index is the size of the window and the value is the maximum
  of all minimum of that window size.
    * 7 |---> 1
    * 6 |---> ?
    * 5 |---> ?
    * 4 |---> ?
    * 3 |---> 2
    * 2 |---> 3
    * 1 |---> 13

  * Observe that there are these unfilled values.
  * The key here is, if the size of the window gets smaller, then the minimum gets larger, because
  the smaller window is a sub-interval of the larger window.
  * there are 3 window in the array with size of 5.
    * `[0 --> 4]`, `[1 --> 5]`, `[2 --> 7]` which belongs to sub intervals with length 6:
    * `[0 --> 5]`, `[1 --> 6]`

  * Therefore, the lower bound is determine by the larger interval, since for window with size 5,
  it's underdeterined (**Proof needed here it's kinda complicated**), we assert that, for all the
  underdetermined sliding window with a size:

    * ans[i] = max(ans[i + 1], ans[i])  # huh... why is it the max of TWO of them...
    * I have no idea why, but this is how the correct algorithm works.

### What Kind of Dark Magic is Going Here

* For the global minimum, the window size of the element is `n`

* For the second minimum in the array, the size of the window must be <= `n - 1`
  * It's equal when the second, first minimum is at the opposite side of the array.
  * If it's not the above case, then the window size it's strictly less than that. In that case, the maximum of
  window size n - 1 will not be in the final array we found.
  * It still works if there are repeated element in the array.
  * If the first and second smallest element is not at the `0`, and `n - 1` index of the array, then the max min of
  window size of n - 1 will be the same as the global minimum. (Because that window will have to include them at some
  point)
* Inductively, for the `k`th smallest element, the max window size for that element, is `<= n - k`

## A Formal Argument

* Basic Definitions:
  * Let `arr` be the array we are looking at.
  * Let, `Min1 <= Min2 <= Min3` be the smallest 3 elements in the array.
  * Def  `F[I]` be a function that map the element in array to the maximum window size such that, the element `I` remains
  to be the minimum of tha window.
  * `n` the size of the array.
  * Def `Soln[I]` to be the solution for the problem, in this case, the the max min of all window size of `I` in the
  array.
* Hypothesis:
  * For all element in array, say `I`, `F[I]` never equals to `n - 1` or `n - 2`.
* Claim 1: F[Min1] = n, F[Min2] <= n - 1, F[Min3] <= n + 2
  * For Min1, there exists no other elements smaller than it.
  * For Min2, there eixists Min1 that is smaller than it, they are at most, `n - 1` slots apart in the `arr`.
  * For Min3, it follows.
* Claim 2: if F[I] = K, then for all windows size that is less than K, the max min of the window size is **at least** I.
  * for contradiction assume that, there eixsts a window with size less than K and with I in it, then F[I] should be
  that number, and not K.
* Claim 2.1: The solution sequence `Soln` has to be Monotonic Decreasing.
  * For contradiction assume: there exists `J`: `Soln[J] < Soln[J + 1]`, Among all windows with size `J + 1`, take
  that element makes it larger than Soln[J], then there eixsts a smaller window of length `J - 1` that contain
  the element too, which, contradicts the statement.

### A more involved example by hand

* Arr = "3 5 4 7 6 2"
         0 1 2 3 4 5
* Immediate left smaller:  `[-1, 0, 0, 2, 2,-1]`
* Immediate right smaller: `[ 5, 2, 5, 4, 5, 6]`
* Window size:             `[ 5, 1, 4, 1, 2, 6]`
* Maximum for each window size:
  * 1 |--> 7  # Cannot be ? because it's the global maximum
  * 2 |--> 6
  * 3 |--> ?
  * 4 |--> 4
  * 5 |--> 3
  * 6 |--> 2  # cannot be ? becaues it's the global Minimum
    * Fact:
      * Monotonically Decreasing as the window's size goes up.
* Then, the maximum of windows size 3 is the max of 4, 5, which is 4.

* See codes for more on how this is handled.

### Extension of the problem

* The maximum for all the window sizes, and we are looking for the minimum for each of the window's
size.
