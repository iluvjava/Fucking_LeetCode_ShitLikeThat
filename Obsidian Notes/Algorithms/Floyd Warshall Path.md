## Intro
* This algorithm looks for the shortest path on a weighted digraph for all pairs of number, and it has a complexity of $O(N^3)$
* This algorithm is inspired by the idea of Transitive Closure in [[Graph and Relations]]. 
* This algorithm also uses the design paradigm for algorithm: [[Dynamic Programming]]
* [Wiki link](https://www.wikiwand.com/en/Floyd%E2%80%93Warshall_algorithm)
### Agorithm
* Denote w(i, j) to be the weight of the edge (i, j)
* Denote a recursive relations for the `ShortPath` function: 
	* Initialization: `shortPath(i, j, 0) = w(i, j)`
	* DP Build: `shortPath(i, j, k) = min(shortPath(i, j, k - 1), shortPath(i, k, k - 1)+shortPath(k, j, k - 1))`
	* And using the idea of transitive closure in mind, we can interpret the function `shortPath(i,j,k)` as the: shortest path with a length at most k that goes from `i` to `j`. 
* Negative Cycles
	* Negative cycles appears as negative numbers on the diagonal of the path matrix, after nth ilterations of the algorithm. 
	* The negative diagonal element is indicating a path that start and ends with the same vertex while having a negative sum. 


### Building the Paths
* In the above example, it only produces the length of the shortest path between all pairs of edges, but if we need the actual path then we need to do something extra by storing the paths as we iterating through it. 
* We will ned another matrix that stores that paths, and then in the recursive case, we join the paths together as we build up the DP. 