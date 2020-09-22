## BFS
* Using a queue to store the vertices, it's a search algorithm on directed graph.

### BFS Exploited
* Path finding, even with multiple vertices. The depth labeling of verteices of the BFS tree is the same as the shortest path if the given graph has unweighted edges. [[Find Nearest Clone]]
* Depth of the tree also can do some kind of spreading simulations, see this problem: [[Rotting-Oranges]], and the depth of the BFS tree determine how long it takes to "spread" to certain vertices. 
* BFS with multiple vertices is as simple as just initiate the queue with multiple vertices in it at the beginning. [[Rotting-Oranges]]


### Codes
* Adjlist is a map of list, starting startingVertices is a list of vertices to start the search with. 
```python
def BFS(startingVertices, adjlist):
	Visited = set(startingVertices)
	Depth = dict((V, 0) for V in startingVertices)
	while startingVertices:
		V = startingVertices.pop()
		for Neighbour in adjlist[V]:
			visited.add(Neighbour)
			startingVertices.append(Neighbour)
			Depth[Neighrbour] = Depth[V] + 1
	return Depth
```
* The above algorithm does a BFS and return a map: Vertices |---> Depth on the BFS tree. 

### Data Structrue
* [[Queue]]