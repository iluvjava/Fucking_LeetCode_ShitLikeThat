# Problem Statement

* Input: A list edges, undirected.

* Output, an edge such that, if removed, breaks the graph into unconnected components, return all such edges
in the graph.

* This problem is testing on the DFS, and Connected Components of a graph.

## Easily Working But Non-Optimal solution

* For each edges in the goraph, breaks it and then do a DFS to see if the graph is still connected, do that for all the
edges in the graph, so that we know, all the edges such that, removing it cause the graph breaks in the CCs.

## Articulation Point

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

## Articulation Edge

* We should find a way to vary the soluiton for the articulation vertex to sole the articulation edge problem.

* Suppose that, `T` is the DFS tree formed by the DFS search.

* For each vertex in the graph, we need the following information:

  * A set, say `S1` representing all the vertices that comes before the current vertex on the DFS tree.
  * A set, say `S2` representing all the vertices that is on all of the sub tree.
  * A say, say `S3` representing all the vertices such that, there eixsts an edge in G that has a connection to, via
  edges that comes after the vertex in the tree.

* This is too complicated to implement and I don't recommend doing this.

* Observe the following, when traversing the tree, a path that lead from the root to the current vertex is matained.

* When recursing back, collect all the vetices that is reachable by the current vertices using edges in the original
graph but not in the tree, then, at step when recursing forward, we know whehter, current vertex is either:
  * Reachable by vertex down the recursion tree,
  * The above is false, then the current edges is an critical edge.
  * NOPE, it cannot be efficient enough due the the set operations.

## Algorithms Implementation Details

* Recursion is going to be our friend and let's hope that we don't get into stack overflow problem.

* Earliest vertex that is connected by the backedges, the efficient algorithm is using the deth as the crucial
information to find the articuatlion vertex.

* Assume the following is know.
  * The DFS tree.
  * For all vertices on the DFS tree, we know which level of depth it's on the DFS tree.

```
foreach (Vertex V on the tree)
  if (The furthest Backwards edges of the sub tree rooted at its children points futher than its child, V --> C
  via edges in graph and not in the DFS tree):
    Then: The edge V <--> C on G is NOT the critical edge.
```

* Let's locate `L` on the furthest part of the DFS tree and assume to cases.
  * `L` doesn't have any backwards edges on G and not in DFS tree:
    * Then, the edge the vertex uses to connect to the tree is a bridge.
    * Then, the furthest Level this vertex points backwards is: itself.
    * Then, for its parent, it will know that its children doesn't have any vertex further down the
    tree that points further back than `L` itself, whicn means that, the edge is again, the
    critical edge.
  * `L` does have edges that are in G, and not in DFS tree, then:
    * The edge connecting `L` to its parent is not the articulation point.
    * The edge points beyond it's parent, to ancestor futher down the tree, and it must be on the
    same branch by the DFS tree invariant.
    * For it's parent, say `P`, will detect that, the sub tree rooted in it's children `L`, has
    an edge ponts back to it's ancester/parent, hence, the current edge `P <---> L` is not the
    bridge on the graph.
  * This concludes the **base case**

* Recursively assert the invariant:
  * The Invariant we want to assert is:
    * For each vertex, we want to know for all vertices under the subtree, the lowest level it points they can point
    back to via edges in G and not in DFS tree.
  * Define a map: `Vertices on DFS ---> Their Level on the tree`, name it `LevelMap`.
  * Define another map: `FurthestBackMap` as a
  `Vertices on DFS ---> furthest point the rooted sub tree points back on the DFS tree`

    * foreach vertex `V`, recursively assert that:
      * `FurthestBackMap[V] := min(The furthest V can points back to, the furthest all it's child's sub tree and points back to)`
      ```
      FurthestBackMap[V] := min
      (
        min(LevelMap[U] for all (V, U) in G not in DFS Tree),
        min(FurthestBackMap[C] for all C of V)
      )
      ```
 
