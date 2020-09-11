# Problem Statement

* Inputs: **Undirected Weighted** Graph
  * A list of cities that must be disconnected from the rest of the graph.

* Output: An integer
  * An integer that represents the minimum time it takes to diconnect the set of vertices from the rest of rhe graph.

* Hint: There is a unique graph between an pair of cities.
  * If this is the case, then the graph has to be a **tree**
  * The tree is free form, and any vertex can be treated as root for the tree.

* Rephrase the problem in a more precise way:
  * Given a tree, weighted with undirected edges, and a set of vertices, say S.
  * Determine an integer, such that, the integer is the sum of all the weights of the edges to remove, so that, for
  all the vertices in the set S, there doesn't exist a path between them, and the weight of all the edges is minimum.

## Idea 1, a random first guess

* Foreach of the red vertex (The the vertices needs to be disconnected from the rest), do a tree serach(dfs) and look
another red vertex, and the find the minimum weight edge in that path and remove it.

* Do this for all the red vertices until all of them are diconnected from the rest.

* This is going to take a lot of time, how can we improve this, or how correct is this solution any way...?

## Idea 1.1, Improving the first Solution

* So I did the problem in paper, because of the tree property of the graph, really, nothing fancy is needed.

* Do a DFS search, rooted at a red (The vertex containig the machines) vertex, and we can recover all the paths
from the root vertex to all the other red vertex, and that will be all the paths regardless of which red root
vertex we choose to start the search.

* Let's say that, there are 4 red vertices in the graph and we manage to recover them in a Tree DFS (If DFS failed then
that is just not a tree). Red vertext noted as X, and other vertices noted as O.
  * X -- O -- O -- X -- O -- X
    * We have 2 cuts, we choose the minimum of them between the Xs and then that, is the minimum cuts needed
    for the problem.
    * get a series of edges between each pair of the X in the path, then find the bottle neck edge for that partial
    route.

## Idea 1.2, Improving the last one (Faild)

* Instead of looking for all the paths, I suggest we just do the search, and record the path information while
recurring, once a red vertex is met, then we can do the back tracing and figure out which each to delete on the path
we traversed.

* Do the recursion, DFS, rooted on a red vertex,
and then add the vertices to the path, and add the edges with weights to a dictionary for look up later.
  * while searching, if the vertex we are looking at is red
    * Traverse bak to the last red vertex and then find the minimum edge, and then add that to our minimum weight.

* This idea failed because the same edges can be chosen multiple times.

## MST Method

* Make a spanning tree that is as expensive as possible while keeping all the red vertex apart from each other.

* Or the equivelent is, joining components with edges in ascending order as long as **at most** one of the edge set has a
machine in it (This will retain the invartiant that, for each connected components, there is only **one** machine
node in it).
  * We need to use the union join data-structure.