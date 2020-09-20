# Problem Statement

* In a given grid, each cell can have one of three values:
  * the value 0 representing an empty cell;
  * the value 1 representing a fresh orange;
  * the value 2 representing a rotten orange.

* Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
* Return the minimum number of minutes that must elapse until no cell has a fresh orange.
  If this is impossible, return -1 instead.

## Idea 1 (brute force simulation)

* This is gonna be linear to the are of the grid and the total number of time frame for the simulation.

## Idea 2 (DFS...? )

* Use DFS to find the deepest branch on all connected components. 

* Record the deepest branching for all of the connected components on the graph. 
  * Rotten oranges is like: Visited. 
  * The not rotten one is like: Not visited yet. 

* 
