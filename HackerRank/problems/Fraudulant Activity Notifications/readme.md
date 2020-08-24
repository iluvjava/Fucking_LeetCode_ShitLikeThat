## Information From Problem Statement

* Assuming you have read the problem statement. <a href="https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting">here</a>

* The problem gives a window size of `d` on the array, and it slides the window across the array, keeping track of the 
median of all numbers that are in the window.

* If any incoming number to the window is 2 times larger than the median inside, then there we need to increment 
the number of "fraudulent activities".

* Obseve that, all possible numbers in the array is very small, and its stated as between 0 and 200, inclusive.

## Idea 1

* Use an array of fixed size to keep track of the median, this requires some really big brain solution.
* Meticulous Design is needed and it will work great if it works. 
* 

## Idea 2

* Use a min, max heap to keep track of the median, and the heap better supports removal of elements. 

