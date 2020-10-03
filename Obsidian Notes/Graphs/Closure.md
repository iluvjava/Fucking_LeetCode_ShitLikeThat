Closure, given any relation $R$, we are interested in the minimal set such that it contains the set $R$ and yet mantain some desired properties from relations

---

Prereq: [[Graph and Relations]]

---

#### Closures
* **Reflexive Closure on** $A\times A$
	* Let $\Delta =\{(a, a)\in A\}$
	* Then $R\cup \Delta$ is the minimal reflexive relations that contains $R$ among all other relations such that, it contains $R$ and it's reflexive.
	* Example: 
		* $R:= \{(a, b): a< b\}$, then $R\cup \Delta$ means $\{(a, b): a \leq b\}$
*  **Symmetric Closure**
	*  Given relation $R$ on $A\times A$, we are interested in finding the minimum symmetric relation that contains relation $R$. 
	*  For each pair $(a, b)\in R$, if $(b, a)\not\in R$, then add it too it, then, the resulting relation is the minimal symmetric relation that contains $R$. 
	*  Using matrice, given $M$ representing $R$, then the $M\oplus M^T$, where $\oplus$ here is the elementwiese OR operator.
	*  It can also be constructed via $R\cup R^{-1}$ where the inverse of a given relations is just reversing the order of the tuples in the relation.
*  **Transitive Closure**
	*  Let's assume again that $R$ is a relation on a graph and $(a, b)\in R$ if there exists path starts with $u$ and ends with $v$.
	*  $R^* = \bigcup_{n=1}^\infty R^n$, is a relation where, if $(a,b)\in R^*$ then there eixsts at path of length at least 1 that connects vertex $a$ and vertex $b$.
	* $R^*$ is the transitive closure of $R$, meaning that for all transitive relation containg $R$, it must also contains $R^*$. 
	* To show $R^*$ is a transitive closuer of $R$, we need to show that: 
		1. $R^*$ is transitive
		2.  $R^*\subseteq S$ whenever $S$ is transitive and it contains $R$.
		*  $R^*$ is transitive because if $(a, b)\in R^*$ then there eixsts a path from $a$ to $b$, and $(b, c)\in R$ then there eixsts a path from $b$ to $c$, hence there eixsts a path from $a$ to $c$.
		*  Let $S$ be a transitive relation containing $R$, then $\forall n \in \mathbb{N}\;S^n \subseteq S$ and $S^*\subseteq S$; By hypothesis we know that $R\subseteq S$, which means that $R^*\subseteq S^*$, which means that $R^*\subseteq S^*\subseteq S$, hence, any transitive relations containing $R$  will contain $R^*$. 
		*  Notice that, we discuss the case $R^*$ as an infinite union of $R^n$ under the context of relations, but under the context of graph, it's perfectly fine to reduce it to $R^* = R^{|V|}$, because if it's longer than that then there is gonna be cycles in the path, which makes it a walk instead of a path. 
	* Given a matrix representation of a finite transitive relation of $R$, say $M$, we can use the boolean matrix to compute the transitive closure of the graph, simply by doing: $\bigvee_{k = 1}^n M^k$
	* Using the naive matrix multiplication, we can get the complexity for the transitive closure algorithm as: $\mathcal{O}(n^4)$
	* Psuedo Codes
	![[Transitive Closure.png]] *Image from: Discrete Mathematics and it's Application 9.4 Transitive closure*
	Note: The $\odot$ is the binary matrix multiplications


---
#### Warshall's Algorithm
* An efficient algorithm for computing transitive closure for finite relations
* **Interior Vertices of Path:** All vertices that are not part of the starting and ending vertex on the graph.
* Let's take a closer look, beginning by denoting the boolean relational matrix $W_p$ for the relation $R^p$ 
	* Lemma: 
		$$(W_p)_{i, j} =(W_{p - 1})_{i, j} \vee 
		\left(
			(W_{p - 1})_{i, k} 
			\wedge
			(W_{p - 1})_{k, j}
		\right)$$
	* There eixists a path with a length of at most $k$ between the vertices indexed by $i, j$ iff there already eists a path with length $k - 1$ or the case that: 
		* There eixsts a vertex indexed by $k$ such that, there is a path with length at most $k-1$ that goes through $k$ from $i$ to $j$. 
		* By transitive closure, the second case doesn't include paths longer than $k$; $R_{p - 1}\subseteq R_{p}$, or using vertex outside of the set of interior vertices.
	* Using this lemma, we can compute $W_p$ with only $W_{p-1}$, reducing the complexity of $\bigvee$ for all the matrices. 
* Psuodo Codes: ![[Warshall Algorithm.png]] *from: Discrete Mathematics and its Applications*
* Outter loop executes n times, and the nested inner loops executes $n^2$, giving a complexity of $O(n^3)$ 
* This is related to one of the graph algorithms for finding the all pairs shortest path called "Floyd Warshall's Shortest Path algorithm", see [[Graph Algorithms]] for more
