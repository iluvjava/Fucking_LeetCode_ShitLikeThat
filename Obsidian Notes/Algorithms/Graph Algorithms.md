# Graph Algorithms

* Algorithm that common got run on a graph
* A graph is usually stored in a hash map, as an adjacency list, the most widely used option for graphs, [[Hash Map]]. 
* [[Code Vault]] Visit here for actual running codes

## Beginner Graph Algorithms:
* DFS: [[Depth First Search]]
* BFS:  [[Breadth First Seach]]


## Advanced
* MST: Minimum Spanning Tree 
	* [[Matrix]]
	* [[Roads and Libraries]]; This is using the porperty of MST, the actual algorithm is not used. 
	* MST: It is the spanning subgraph with the minimum amount of edges, If any additional edges were to remove from the graph, then the graph becomes disconnected.
	* Data Structure needed: [[Union Find]]
* Top Sort: Topological Sorting
	* Khan Top Sort
	* Periority Queue 
	* DFS Reverse Backtracking
* Shortest Path Finding
	* [[Bellmand Ford]] General Shortest Path from `s` to `t`
	* [[Floyd Warshall Path]]: General Shortest Path for all pairs
	* Dijkstra: Greedy Path [[Greedy Algorithm]]: Positive Edge weight
		* This one is too famous, however, I didn't see it popping up in coding challenges.
		* Data Structure got used: [[Heap, Priority Queue]]
	* A*: Spatial Greedy Path: Points in Space
	* Johnson's Shortest Path: Bellmand Ford + Dijkstra algorithm with pontential graph and path conversin
* Turtle and Hare Cycle Detection
	* Given a function that is a mapping from its domain to the domain itself. 
		* Determine whether there is a cycle
		* Find the cycle length if there is
		* Find the starting point of the cycle. 
	* This algorithm has its first application of looking for the period, and the starting point of the cycle in a psuedo random number generator efficiently. 

### Kruskal Algorithm of Minimum Spanning Tree
* Algorithm leverage the usage of a special type of data structure call: "Union find" or "Disjoint Set". see [[Union Find]]
	* This is used for the algorithm to union set of vertices together to keep track of the connected tree in the graph while adding edges. 
	* This is the pivotal problem that spawn the idea of a **Matroid**. 
	* This is a [[Greedy Algorithm]], where, we sort all the edges in the graph and then we add them to the graph while keeping all the connected components on the graph to be a Tree.

## Super Advanced
* Network Flow: Ford Fulkerson
	* Max Bipartile Matching
* Path Finding: 
	* Augmentation of above algorithms and applications of those algorithms 
* Perfect Matching
* NP-Hard Graph Problems
	* TSP


## Misc

* Foyd Cycle Detection
* This algorithm is really smart and I want to talk about it. 
	* Phase I: identify the cycle
	* Phase II: Find the starting point of the cycle
	* Phase III: Identify the length of the cycle
