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
* Iterative implementation where repeated vertices might appear in the stack, for a vertex, it happens when its neighours are direct neighbours of each other.
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
	def DFS(startingVertex, adjlist):
		Stack = [StartingVertex]
		Visited = set([StartingVertex])
		LastNeibour = {}
		# remembers the last neigbour put into the stack.
		while Stack:
			V = Stack[-1]
			Visited.add(V)
			if V not in LastNeighbour:
				LastNeighbour[V] = 0
			if LastNeighbour[V] < len(Adjlist[V]):
				Stack.append(adjlist[LastNeighbour[V]])
				LastNeighbour[V] += 1
			else:
				Stack.pop()
			
	```
	

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

## Data Structure
* [[Stack]]