## How I Failed:

* I cannot solve this problem passing all the testcases. The speed is a problem for me.

* I didn't realized the additional constraints that the indices of the triplets are in the format of
: **i < j < k**, which is important for tightening the run-time of the solution.

## Random Idea 1 (Failed)

* When traversing the array, and querying "x", we are not interested in "x^2, x^3" appeared before the array, we are
only interested in then appearing after the array.

* The sequence are are insterested in is fixed by inputs of r: `[1, r, r**2, r**3...]`.

* when traversing backwards, let the element we are currently looking at be: x:

  * if x is in the geometric sequence, then we look for the number of appearences observed for `x**2`, and `x**3`.

  * say they are `m`, `n`, then we have `m*n` possible triplets.

  * Increment the number of appearances for `x` too.

## Implementations

* I will write it in python first before writing it in java.

## Submission Failed

```
def soln(arr, r):
    Max = max(arr)
    FreqDic = {}
    GeoSeq = set()
    G = 1

    while G <= Max:
        GeoSeq.add(G)
        G *= r
    del G  # name scape polution.
    Counter = 0
    for I in reversed(arr):
        if I in GeoSeq:
            if I not in FreqDic:
                FreqDic[I] = 1
            else:
                FreqDic[I] += 1
            Counter += FreqDic.get(I*r, 0)*FreqDic.get(I*r*r, 0)
    return Counter
```

* Questions: Is it true that, the geometric sequence doesn't have to start with 1? And the start of the sequence, a0,
can be any number in the array?

* Yes, it seems to be the case.

* What is wrong with this solution? This solutin gives the wrong answers.

```
def soln(arr, r):
    FreqDic = {}
    Counter = 0
    for I in reversed(arr):
        if I not in FreqDic:
            FreqDic[I] = 1
        else:
            FreqDic[I] += 1
        Counter += FreqDic.get(I*r, 0)*FreqDic.get(I*r*r, 0)
    return Counter
```

* This solution is wrong because, when traversing, say we have I at index i, but the ordering information for
I*r and I*r*r are lost, the indeices for those number in the geometric sequence could be out of order,
hence the solution ultimately will be an over estimation.

## Random Idea 2 (FAILED)

* given x, we know the number of paris of `x*r` and `x*r*r`, where `x*r` comes before `x*r*r`. Nope.

* Give x, what if knew the number of appareances of `x*r` and `x*r*r` right after `x`?
  * FreqDic is a mapping from (x) |---> (a, b), where a is the frequencies of `x*r` that comes after `x`, and b is the
  frequency of `x*r*r`.
  * `FreqDic[x][0]*FreqDic[x*r][0]` Gives all the triplets from after `x`.
  * How to update?

## Random Idea 3 (FAILED)

* What if, we just crate a map: (x) |---> List[int] where the list is all the indices that the element appeared at in the
array?
* Assume the map is created while traversing the array in reverse, then, given `x` at `I`, for all J in `m[x*r]`, get
list `m[x*r*r]`, sum all occurances of index that is larger than `J`.
* This is provably correct from how we defined things.

## Random Idea 4 (FAILED)

* create a map: (x, y) |---> z, where `x` is the element in the array, and the `y` is an index in the array, `z` is the
number of appearances of `x` after the index `y`.
* Nope.

## Random Idea 5 (FAILED BUT CLOSE)

* Create a map (x) |---> (a), where `a` is the number of tuples (i, j) comes after x in the array where `arr[i]` is `x*r`
and `arr[j]` is `x*r*r`, and, `i < j`.

* Assuming the map is kept while traversing in the reverse order.

* Given x during traversal, `m[x]` gives the number of triplets involving current element x.

* `x` is an new instance, and we need to update it, it adds tuple counts to: `x, x*r`, and the thing comes before it
will be `x/r`

 * The number of `x, x*r` is the number of occurances of `x*r` if x never appears.

 * if x already appeared, then we add that `x*r` to the existing value in the dictionary.

* **ONLY ONE TESTCASE FAILED FOR THIS IDEA** ...
  * I have no idea one it failed specifically for hidden Testcase 6, and the output is: `690302634` and expected
  value is `2325652489`.

## Ideal 5.1 (Worked)

* Create map `m`: (x) |---> (a) where `a` denotes the number of tuples (i, j) comes after the element x in the array, with
i < j, and the `arr[i]` is `x`, and `arr[j]` is `x*r`.

* Traversing the element in reversed order, let `X` be the current element:
  * then `m[X*r]` is the number of tuples of `x*r, x*r*r` after `X`.
    * `Counter += m.get(X*r, 0)`
  * The new element X is part of the tuple: `X, X*r`, corresponds to the key: `X`. The number of such tuples is given
  as: `m[X]`, and the additional number of tuple is computer via `m[X] + "The number of occurences of element X*r"`.

* The number of occurences of all elements in the array while traversing in reversed order need to be kept in another
map data structure.

## Moral of the Story (Corollary)

* This can be phrased generally as: "Given a sequence of symbols, find all 3 non-continous sub sequences that satisfy
certain conditions.", the conditions are phrased in such a way that, given any element, the element immdiately next
to that element can be determined by what element comes before it.

* Keys:
  * Ordering of the non-continous subsequence.
  * Counting the number of occurancesof the discontinuous sequences.
  * Using the map to do the things.

* Extension:
  * If we are looking more than a triplets, say quadruples of `x, x*r, x*r**2, x*r**3`, def m: (x) |---> y where y is
  the number of triplets `(x, x*r, x*r**2)` that comes after x.
    * Then the additional number of qudruples of `(x, x*r, x*r**2, x*r**3)` is `m[x*r]`
    * x is the start of the triplets: `(x, x*r, x*r**2)`, the additional number of such triplets are given by:
    `x` multiplied by the number of tuples: `(x*r, x*r**2)`, so we need another dictionary to keep track of all the
    tuples.
      * The problem becomes similar to couting the number of triplets.
      * Apply recursion here, then we have a general solution to any tupe of discontinous subsequences.

  * Choice to store other relavent information about the discontinous subsequences give solution to different 
  problems and requirements for outputs.