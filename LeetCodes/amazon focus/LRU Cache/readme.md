# Problem Statement

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

* And then, we keep a bi-directional map: from ID <---> Key Value Pair
  