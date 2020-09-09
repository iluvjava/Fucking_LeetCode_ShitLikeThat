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

# Idea 1, a random first guess

* Foreach of the red vertex (The the vertices needs to be disconnected from the rest), do a tree serach(dfs) and look
another red vertex, and the find the minimum weight edge in that path and remove it.

* Do this for all the red vertices until all of them are diconnected from the rest.

* This is going to take a lot of time, how can we improve this, or how correct is this solution any way...?
