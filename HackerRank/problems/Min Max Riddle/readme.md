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