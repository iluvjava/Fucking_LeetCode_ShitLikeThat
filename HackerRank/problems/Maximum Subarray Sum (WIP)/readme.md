# Problem Statement

* Given array of integers.

* Given a integers m, positive, larger than zero.

* among all the possible sub array, we sum them up and modulo the integer m, we are interested in the largest
numbers among all the sub arrays. The sub-arrays are discontinous.

* Useful information from the constraints of the problem:
  * All the numebrs in the array are positive intergers and they are non-zero
  * All the numbers in the array are in the range of `0 < a < m`, this might be important

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

## Random Ideas

* Observe how, all the elements in the array are going to be smaller than the given modulo.

* T[I, K] := "whether the sub array starting from 0 to I has a sub array that sums up exactly to K."

* T[I + 1, K]
  * If `arr[I + 1]` is one of element in the solution sub-array
    * T[I + 1, K] = T[I, K - arr[I + 1]]
    * Here, `K - arr[I + 1]` can be negative. If that is the case, it means that, m - (K - arr[I + 1]) is what we
    are interested instead, because of the modulo operations.
    * Else, if it's not negative, then the recurrence just passes over.

  * if `arr[I + 1]` is not one of the element in the solution sub-array
    * T[I + 1, K] = T[I, K]

* Repeat the dynamic programming process for all the possible values, then we find the maximum one that has 
a possible sum for. 