# Problem Statement

* In a given grid, each cell can have one of three values:
  * the value 0 representing an empty cell;
  * the value 1 representing a fresh orange;
  * the value 2 representing a rotten orange.

* Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
* Return the minimum number of minutes that must elapse until no cell has a fresh orange.
  If this is impossible, return -1 instead.

* So all the rotten tomatoes start rotting simultaneously, and then we are going to find the day when
all of the tomatoes are rotten.

* Edges cases to consider:
  * What if there are no rotton tomatoes to begin with?
    * Then return -1
  * What if all tomatoes are rotton?
    * Then return 0
  * What if that there are tomatoes that are just not connected with the rotten one?
    * Then just return -1

## Idea 1 (brute force simulation)

* This is gonna be linear to the are of the grid and the total number of time frame for the simulation.

* Worst time is probably gonna by cubic complexity. 

## Idea 2 (DFS...? )

* Use DFS to find the deepest branch on all connected components.

* Record the deepest branching for all of the connected components on the graph.
  * Rotten oranges is like: Visited.
  * The not rotten one is like: Not visited yet.

## Idea 3, the Correct Exploit: Depth of BFS and Intialization of multiple vertices

* There is a key that I missed in the BFS algorithm is the, initizlizing with multiple vertices that are not adjacent
to each other in the queue is entirely possible and the BFS will **run in parallel** in that case.

* Another key exploit here is the depth of the tree for each vertex on the tree, which will be constructed for
each of the vertices in the arr while running the BFS algorithm.

* Yep. this is the correct way to solve it. 
