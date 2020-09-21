# Graph Algorithms

* Algorithm that common got run on a graph
* [[Code Vaults]] Visit here for actual running codes

## Beginner Graph Algorithms:
* DFS: [[Depth First Search]]
* BFS:  [[Breadth First Seach]]

* Both algorithm shared the same structure, but they uses different data structure to keep track of the vertices. 
* Here is the generic codes for both routine:
```
Initialize: QueueStack  # Queue if BFS, stack if DFS
while (QueueStack has Vertext):
	V = QueueStack.get() 
	foreach (U as Neibours of V):
		if (U is not visted):
			MarkVisited(U)
			QueueStack.add(U)
```


## Advanced
* MST: Minimum Spanning Tree 
	* [[Matrix]]
* Top Sort: Topological Sorting
* Path Finding
	* Bellmand Ford: General Shortest Path
	* Dijkstra: Greedy Path
		* This is too famous to described, however, I didn't see it popping up in coding challenges
		* Data Structure got used: [[Heap, Priority Queue]]
	* A Start: Special Greedy Path

### Kruskal Algorithm of Minimum Spanning Tree
* Algorithm leverage the usage of a special type of data structure call: "Union find" or "Disjoint Set". 
	* This is used for the algorithm to union set of vertices together to keep track of the connected tree in the graph while adding edges. 
	* This is the pivotal problem that spawn the idea of a **Matroid**. 
	* This is a [[Greedy Algorithm]], where, we sort all the edges in the graph and then we add them to the graph while keeping all the connected components on the graph to be a Tree.

## Super Advanced
* Network Flow: Ford Fulkerson
	* Max Bipartile Matching
* Path Finding: 
	* Bellmand Ford + Dijkstra
* Shortest Path on DAG