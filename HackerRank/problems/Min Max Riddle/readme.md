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

* [Geek link]()

### Reasoning

* For each of the element `arr[I]` in the array, we find the nearest smaller element on its left and right, say
`arr[K] < arr[I], arr[J] < arr[I]` where, `K > J`

* Then, we know that, for all window sizes, s such that `1 <= K <= K - J`, the element `arr[I]` is going to be the
minimum of those window sizes.

* To look for, 2 arrays of indices that denotes the immediate smaller element on the left and right of the element
at `I` we use the similar stack strategies described in `..\Largest Reactangle`
  * 

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
   
    * ans[i] = max(ans[i + 1], ans[i + 2])
    * Note that, the global minimum eixsts, hence, the quantity is defined. 

### A more involved example by hand: 

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

* See codes for more on how this is handled. 


### Extension of the problem

* The maximum for all the window sizes, and we are looking for the minimum for each of the window's 
size. 
