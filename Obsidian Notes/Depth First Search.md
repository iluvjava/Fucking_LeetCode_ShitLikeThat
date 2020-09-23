# Depth First Search

* Using a stack to keep track of the vertices
* The DFS algorithm heads in one line, straight into the graph until: 
	* There is no more neighbours on the given vertice.
	* OR, all the neighbours on the current vertex has been visited. 

## Codes
* The DFS algorithm is kind complicated, the easiest way to implement it is via recursion and backtracking:
* Recursive Implementations:
	```python
	def DFS(startingVertex, adjlist, visited = None):
		visited = set() if visited is None else visited
		visited.add(startingVertex)
		for Neighbour in adjlist[startingVertex]:
			if Neighbour not in visited:
				DFS(Neighbour, adjlist, visited)
	```
* Iterative implementation where repeated vertices might appear in the stack, for a vertex, it happens when its neighours are direct neighbours of each other, or, some vertex visited in the future share the same neighours as the current vertex in the iteration. 
	```python
	def DFS(startingVertex, adjlist):
		Stack = [startingVertex]
		Visited = set([startingVertex])
		while Stack:
			V = Stack.pop()
			if V not in Visited:
				for Neighbour in adjlist[V]:
					Stack.push(Neighbour)
	```
* Another iterative solution will let the vertex remembers to continue with the last neighours, so vertex acts like an iterator of its neighbours.
* The level map of the DFS tree can be very useful, and it's applied to many places. 
	```python
	def DFS_iterative(root, adjlist):
		NextNeighbours = {}
		for V, _ in adjlist.items():
			NextNeighbours[V] = 0
		Stack = [root]
		Visited = set()
		Depth = {}
		Depth[root] = 0
		while Stack:
			print(f"Stack: {Stack}")
			V = Stack[-1]
			Visited.add(V)
			Exec = False
			while NextNeighbours[V] < len(adjlist[V]):
				Neighbour = adjlist[V][NextNeighbours[V]]
				if Neighbour not in Visited:
					Stack.append(Neighbour)
					NextNeighbours[V] += 1
					Depth[Neighbour] = Depth[V] + 1
					Exec = True
					break
				else:
					NextNeighbours[V] += 1
			if Exec:
				continue
			else:
				Stack.pop()
		return Depth
	```
	
* Please observe the role of `Exec` variable, the `NextNeighours` hashmap, and the role of `beak` clause in the inner while loop. 
* The `NextNeigbhours` variable is a remembers which neighbours in the adjlist the vertex should be adding to the stack next, emulating the effect of an iterator.
* The Inner while loop searches for the first unvisited vertex and then breaks out to the `if` clause, where it detects  the breaking conditions of the inner while loop. The inner while loop can exit with the following conditions: 
	* All Neighbours are visited. 
		* Under this case, the if statement captures it and pop the vertex out of the stack, the life time of the vertex in the stack has been completed. 
	* At least one neighbour remains unvisited
		* Under this case, the if statement captures it and return to the larger while loop, with the unvisited neighbour added to the stack.

### DFS Exploited
* DFS tree
	* The order of visiting the vertices in the graph forms the DFS tree. 
	* For all edges exists in the tree but not in the graph, it connects a vertex to an ancester that is under the same branch.
	* The level map of the tree can be exploited to detect bridges in a graph, and it's featured as the optimal solution for this problem: [[Critical Connection in a Network]]
	* See the Geek geek discussion on a similar propblem: [Articulation Point](https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/)
* Connected Components
	* BFS also does it
	* It can detect the size of connected components given a vertex in the graph.
	* [[DFS-Connected-Cell-in-Grid]]
	* [[Number of Islands]]
* Top Sort
	* DFS can be use to extract the reversely partial sequence of the Topological Ordering of the graph.  

## Data Structures Exploited
* [[Stack]]