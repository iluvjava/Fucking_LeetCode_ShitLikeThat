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


## Implementations:

* I will write it in python first before writing it in java.

## Submission Failed:

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