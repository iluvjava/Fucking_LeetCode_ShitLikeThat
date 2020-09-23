# Problem Statement

* Input: A list edges, undirected.

* Output, an edge such that, if removed, breaks the graph into unconnected components, return all such edges
in the graph.

* This problem is testing on the DFS, and Connected Components of a graph.

## Easily Working But Non-Optimal solution

* For each edges in the goraph, breaks it and then do a DFS to see if the graph is still connected, do that for all the
edges in the graph, so that we know, all the edges such that, removing it cause the graph breaks in the CCs.

## Articulation Point (Discussion of a Similar Problem)

* Given a graph, the point such that, removing the point causes the graph to break into connection component is call
an articulation point.

* DFS:
  * The DFS tree experience structures, such that, for each of the vertex, it will either connect to its parent vertices
  on the same branch, or they connect further down the DFS tree.

* DFS Tree:
  * After the construction of the DFS tree, we consider the edges that are in the graph G, but not in the DFS tree,
  for each vertex on the tree, if there is an edges that points back to its ancestor from the from the vertices below,
  then that vertex cannot be the articulation point of the graph.

* (Geek for Geek Articulation Point)[https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/]
  * Back edges on the DFS tree is the key to looking for the articulation vertices of the tree.
 
## Asserting the Minimum Pointback when doing the DFS traversal on the graph


