# Problem Statement 

* (On HackerRank)[https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming]

* The problem wants us to find a sub-array that is not continuous such that the elements in the 
array has the maximum possible sums. 

* Think: How to relate a problem to its sub-problems. 


## Idea: Iterative Dynamic Programming 

* Assume that, for all seqeunce `arr[:i]` we obtrained the maximum achievable non-adj sum. 
  * NOTE: `arr[:i]` denotes for all `0 <= I < i`

* Then, for the element at index `i`, we had the choice to either include it or not. 

* Denote `T[I]` to be the maximum achievable non-adj sum for the sub array: `arr[:I + 1]`
  
* if `i` th element is in the global optimal, then `i - 1` is not in. 
  * Then we have the choice to either use `T[i - 2]` to improve it. 

* if `i` th element is not in the global optimal, then it follows from the optimal of `T[i - 1]`.

* Recurrences: 
  * T[I] := max(arr[I] + max(T[I - 2], 0), T[I - 1])


### Base case

* T[1], T[0] needs to be defined at the beginning. 
  * T[0] := arr[0]
  * T[1] := max(arr[1], arr[0])
  * T[2] := max(arr[2], arr[1]) + T[0]


### Moral of the story

* When consider the recusrive case, we need to consider the case where, the singleton choice of 
the `i` th element might be able to improve the current solution. 

* Please remeber this recurrences: `T[I] := max(arr[I] + max(T[I - 2], 0), T[I - 1])`,
I will call it "XOR Linear Recur"