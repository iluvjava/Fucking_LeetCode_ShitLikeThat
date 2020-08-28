# Problem Statement

* (Link)[https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs]

* We are given an undirected graph where each vertex, edges are associated with a cost.

* We need to return the cheapest cost of building such a thing.

* A valid Solution is:

  * all the connected componets have a route that leads to a library.

* The costs for building the roads and building the library is the same. The roads are the undirectred edges and the
vertices are the city with/without libraries.

* Some Special Cases to start reasoning with this problem.
  * If roads are free, then for each connected components, build one library and span it with an MST.
  * If libraries are free, then build libraries for all cities and forget about the roads.

* **Roads cost**: c1, **Libries cost**: c2.
  * for each CC:
    * Make MST, assume vertex count to be n
      * |E| = n - 1, |V| = n
      * Build all roads and one library: c1|E| - c2 = c1 * n - c1 + c2
      * Build all libraries and no roads: c2 * n
      * Differences: |(c1 - c2)*n - c1 + c2|

* Consider the fact (The key reasoning):
  * If you disconnect one MST into 2 MSTs, then we have to add a new libraries.
  * If the cost of library is higher, then we have a higher cost, else, we would have reduce the cost.
  * Think of this inductively.

* Therefore, the decision is made purely on whether: c2 > c1, or c1 > c2.

## Algorithm (How to compute the cost)

* If the cost of the libraries and the cost of the roads are the same, then the cost is n * c where n i |V| for the
graph.

* if the cost of the roads is cheaper, then the cost will be: `(n - 1) * c1 + c2`, if the cost of the libraries is cheaper,
then the cost will be: `n*c2`.

* HOWEVER, that is for one connected components only, what about several of them?
  * We need a sub routine that scan for the connected components! and we only need their sizes.

## Scanning for Connected Components for Undirected Graph

* Input type of the queries contain a graph, adjacent list.

* Finding CC: DFS, BFS.

## Problem

* One wrong answer and running out of time for the problems. 