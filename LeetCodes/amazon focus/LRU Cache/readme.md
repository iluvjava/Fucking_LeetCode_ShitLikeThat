# Problem Statement

* (link)[https://leetcode.com/problems/lru-cache/]

* Design a data structure that stores some kind of key value pairs.

* LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

* int get(int key) Return the value of the key if the key exists, otherwise return -1.

* void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the
cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

## Idea1

* Key value pairs using a queue as the underlying mechanics.

## Idea2

* What if, we keep the ID of the element added
  * The ID increments by one when the put() method is called.

* And then, we keep a bi-directional map: from ID <---> Key ---> Value Pair

* Assume that, `M` is the bidirectional map, let's use this to design the data structure.

* Instantiate the following states for our object:
  * `[1: <1, 1>, 2: <2, 2>, 3: <3, 3>]` with the format: `ID: <Key, Value>`
  * Say an update operation occured, `put(1, 4)`, then it gets updated to.
    * `[4: <1, 4>, 2: <2, 2>, 3: <3, 3>]`
    * Operations involved:
      * Find the ID via key, update the value for that key.

* if we want to delet, then we do 4 - 3, to find 1, the ID, then we can delete the key, and the make space for
 the new key value pair and it's ID, which will be: 5.