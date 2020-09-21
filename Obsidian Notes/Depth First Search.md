# Depth First Search

* Using a stack to keep track of the vertices


### DFS Exploited
* DFS tree
	* Formed while doing the DFS searching
	* For all edges exists in the tree but not in the graph, it connects a vertex to an ancester that is under the same branch.
	* The level map of the tree can be exploited to detect bridges in a graph, and it's featured as the optimal solution for this problem: [[Critical Connection in a Network]]
* Connected Components
	* BFS also does it
	* It can detect the size of connected components given a vertex in the graph.
	* [[DFS-Connected-Cell-in-Grid]]
	* [[Number of Islands]]
* Top Sort
	* DFS can be use to extract the reversely partial sequence of the Topological Ordering of the graph.  


## Data Structure
* [[Stack]]