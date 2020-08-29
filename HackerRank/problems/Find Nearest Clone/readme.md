# Problem Statement

* (link)[https://www.hackerrank.com/challenges/find-the-nearest-clone/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs]

* Vertex:
  * Index from 1.
  * With a color.

* Color: Also Indexed from one

* Inputs:
  * Graph
    * undirected, unweighted.
    * CONNECTED!
  * Specific Color
* Oututs:
  * Find the shortest path length connecting that vertex to another vertext of the same color.

## Idea 1 (BFS on all, Super slow)

* dfs for shortest path.

* for each vertex with desired color:
* do a search to find the closest vertex with that color.
* return the minimum finding of the above routine.

### Some Simplifictions

* if the distance is the shortest possible, 1, then return 1 as soon as that happend.
* if the colored vertex we want to earch is unique, then return -1.
* we also need to skip all the vertices that has already been identified, or else, we will alternate between 2
vertices when doing the BFS.

* can we do better? Do we really need to find ALL PAIRS of distances for vertices with that color?

## Idea 2 (Doesn't work)

* Make a psuedo vertex with one edge, connecting to all the colored vertices we are interested in.
  * Doesn't work because the psuedo edges are just too short.


## Idea 3 (Probably won't work)

* Use the levels on the BFS tree.

* Assume we are interested in color blue.
  * If, on the BFS tree, 2 of the blue vertex is one level away from each other, then, the shortest distance between then is 1.
  * if, on the BFS tree, 2 of the blue vertices is 2 level away from each other, then, the shortest distance between
  them is 2.
    * assume other wise, then the shortest distance from the root to the third blue will give a contradiction.

* !!! Like... what if 2 of the blue vertices are on the same level? The distance between then is at least 1, but that will
give us a distance of 0 between them. Hence, the level doesn't tell us that.
  * The distance between thoe 2 vertices can be arbitrarily large, bounded by the sum of their distances to the root.

### Algorithm:

* BFS the whole thing.

* Assign the level for each of the blue vertices.

* Given a sorted seqence of number, look for the sortest.


## Idea 4 (Triangle Inequality works)

* Assuming that, given blue vertex v1, we fond nearest u2 blue vertex.

* Given u2, ignore v1, we find w3 as a blue vertex.

* Then, the distance between v1, w3 is not mininmum.

  * assuming other wise, then v1 should find w3 first, which is a contradiction.

  * Hence we dont' need the distances between all the pairs.

### Algorithm

* We run the BFS, and then once a pair is found, we discolor the first vertex we started with.
  * Proof.
  * Start with v1, get v2, as the shortest distance blue vertex.
  * Ignore v1, start with v2, find the shortest distance blue vertex, say, v3.
  * V2 found before v3, hence dis(v1, v2) > dis(v1, v3).
    * now we can confidently ignore v1.

* And then, we finda new blue vertex, repeat.

* keep the shortest distance during this process.

* Triangle inequality kept us safe.

* By connectivity of the graph, if we can't find any other blue vertices during the process, then that vertex is the
last one.


