# Problem Statement

* Given an 2d array of 1, 0s, where 1 represents the represent of the island, we want to find the number of island
that is in the graph.

* Note: A block is connected to its neibours **Horizontally and Vertically**

## Ideal 1:

* This problem is testing for basic DFS/BFS for counting connected components in the graph.

* For each island in the array, do a BFS search and remove the element from the graph accordingly after visiting, and
do that for all the elements in the 2D array whenever the element in the position is not a 1.

