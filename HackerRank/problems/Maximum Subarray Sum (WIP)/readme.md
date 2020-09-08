# Problem Statement

* Given array of integers.

* Given a integers m, positive, larger than zero.

* among all the possible sub array, we sum them up and modulo the integer m, we are interested in the largest
numbers among all the sub arrays. The sub-arrays are discontinous.

* Useful information from the constraints of the problem:
  * All the numebrs in the array are positive intergers and they are non-zero

* Potential Exploitations
  * Modular Arithematics and repeatitions of elements in the array.
  * The common factors between m and elements in the array.
  * If m are co-prime to all the numbers in the array, then, it's modular will span the whole space.

## Idea 1

* Bruteforce, recursive search, this is graranteed to work correctly, but the complexity will be 2^n and the length
of the array cannot goes beyond 5000 or else stackoverflow.

## Idea 2

* Optimistic Sequential Search with Dynamic programming.

* Variables:
  * `arr` the array given

* The sum of all the sub-array cannot exceed the sum of all the elements in the whole array.

  * for all, `k` such that `0 <= m*k <= sum(arr)`, use DP to look for whether there eixsts such a sub-array that
  has the sum of exactly `m*k`, and `0 <= k < m`.
  
* This is still going to be very slow if the inputs are on the scale of thousands, and yes, it is. 

# Random Ideas 

* 