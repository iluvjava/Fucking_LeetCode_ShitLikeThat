# Things to Start

* Each person can bribe the person in front of them, and only 2 bribes.
  * The maximum relocation of the element is 2.

* `[1, 2, 3, 4]` changed into `[4, 1, 2, 3]` is impossible becaues `4` needs 3 bribes to move 3 positions
  * Output: Too chaotic.

* After: `2, 1, 5, 3, 4`, Original: `1, 2, 3, 4, 5`, difference: `1, -1, 2, -1, -1`, the sum of difference is going
to be zero.
  * `After *- Original` must have all element less than or equal to 2.
  * Sum of all elements is going to be zero, because each bribe involves creating a `-1`, `1` pair, or a `-1, -1`, `2`
  pairs.
    * This should be true in general.

* Each positive number `k` in `After *- Original` indicates at least k bribes (k left adjacent swap) for the element at
the position.

* If this is greedy, then summing up all the positive number will give the minimum number of (k left adjacent swap).

## Try Some Test Cases out on This Notes

```
5
2 1 5 3 4
[2, 1, 5, 3, 4] -* [1, 2, 3, 4, 5]
[1, -1, 2, -1, -1]
```

* Sum of positive inversion: 3

```
5
2 5 1 3 4
[2, 5, 1, 3, 4] -* [1, 2, 3, 4, 5]
[1, 3, -2, -1, -1]
```

* Maximum, positive inversion is beyond 2.

```
[1, 2, 5, 3, 7, 8, 6, 4]
[1, 2, 3, 4, 5, 6, 7, 8]
[0, 0, 2,-1, 2, 2,-1,-4]
```

* Expected to be 7
* Reverse the bribe:
  * [1, 2, 5, 3, 4, 7, 8, 4, 6]
* We didn't see that, 6 bribed 4.
* This failed, we need more observations. 

### The Legit Reasoning 

* Consider this statement: For each person, the total number of people who comes before him but should be after him
is telling us about number of bribes.

* Realize the following things:
  * Mutual bribing is not going to happen, because the problem only allows people bribing people directly in front of them.

* Suppose one of the person who got bribed, then, he can count the number of people who are behind him but got
in front of him, those people who are in front of him are called: Out of order element (OOE).
  
  * For all people behind him who get in front of him, they have to bribe him.
    
    * This is true because each person can only bribe once and move by 1 position to the front of the queue.
  
  * Hence, for that person, he can count the OOE people to know how much money he got.

* Summing up all the OOEs for all people in the queue, we will have all the number of transactions of bribes.

* How it makes sense that, the total number of OOEs are the minum number of inversions? 
  * Because among all possible permutations of ways people can bribe to get 
  in front of the queue, the solution is unique. 


### The optimization
* The process of counting the inversions has a quadratic complexity with bruteforce, but it can be improved with the 
count inversion method using the merge sort algorithm. 
* Use linked list to merge 2 lists. 

#### Counting the Number of Inversions
* Consider the following:  
    * [a1, a3, a4, a2, a5] to be an re-arrangement of the original array. 
    * The number of inversion all pairs of elements that are out of order, they are: (a3, a2), (a4, a2)
* Counting all pairs of inversion in 2 sorted array is easy. 
    * [a1, a3], [a2, a4, a5]
    * [a1, a2, a3, a4, a5], comparison (left, right): <, >, <, one inversion detected. 
    * another example:
    * [a3, a4], [a1, a2], if joined, then [a3, a4, a1, a2], 4 inversions are involved.
        * the sequence of comparison from left to right is: 
        * `>, >`  
            * first comparison: a1 < a2 < a3, so that is +2 inversions. 
            * second comparison: a2 < a3 < a4, so that is + 2 inversions. 
            * 4 inversions in total. 
* Use this idea with merge sort, so we count the number of inversions during the merging process of the algorithm in 
merge sort. 
    * Take this for example.
    * [1, 2, 5, 3, 7, 8, 6, 4]
        * [1, 2, 5, 3], [7, 8, 6, 4]
            * [1, 2], [5, 3], [7, 8], [6, 4]; The branching process for merge sort has now completed.
            * [1, 2], [3, 5], [7, 8], [4, 6]; inversions: 4
        * [1, 2, 3, 5], [4, 6, 7, 8]; inversions: 2
    * [1, 2, 3, 4, 5, 6, 7, 8] inversions 1
    

* Inputs: 
    * A list of elements and the indices for each elements in reference array. 
