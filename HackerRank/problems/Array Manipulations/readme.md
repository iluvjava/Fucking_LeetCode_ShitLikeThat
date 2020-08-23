## Solution

* **I didn't solve this**, I asked my friend and he solved it, but I will record our discussion here.

### Idea 1

* Interval Tree. <a href="https://www.geeksforgeeks.org/interval-tree/">Link</a>
  * The interval tree is a data structure for intervals in any dimension.
  * Given an interval or a set of points, the tree is able to look for a the intervals that includes the points in
  log(n) under the best case. (self balancing can be borrowed from AVL tree)
  * Each node of the tree stores the following:
    * The maximum right boundary for the right subtree.
    * an interval.
    * **Inveriant** : The left subtree's maximum is always less than the right subtree.
  * The idea is, we store the queries as a set of intervals, and each queries.
  will take use to a set of intervals the intersect with the new intervals, then we update the maximum value
  for each interval accordingly.
* Problem:
  * Solution requires a full good implementations of the data structure.

### Idea 2

* Imagine the problem as some sort of, 2d terrain. Where each interval is a block with some height spanning over some
distance.

* The problem is basically asking: "If we gave you these set of intervals and their heights, tell me what is the
maximum height after all the constructions."

```
a b k
1 5 3
4 8 7
6 9 1
```

* When traversing the landscape, we add `k` to a running sum when we met an left boundary of an interval, and we
subtract `k` when we met a right boundary. We keep the maximum of the running sum.

* This requires us to sort all the interval's left and right boundaries.

* And then my friend gave me this codes that passes all test in a matter of moments when I was showering.

```
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    points = []
    for a, b, k in queries:
        points.append((a, k))
        points.append((b + 1, -k))

    maximum = 0
    current = 0
    for _, v in sorted(points):
        current += v
        maximum = max(maximum, current)

    return maximum
```

* Amazing.