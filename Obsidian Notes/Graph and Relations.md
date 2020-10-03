# Graph and Relations
----------------------------------------------
### Relations
* **Def** relation: $R\ \subseteq A\times B$
	* It looks like a directed bipartile graph
* Assume that, $A = B$, so that $R \subseteq A\times A$, then we a relation on the same set it self, here are some examples: 
	* $R_1 = \{(a, b): a \leq b\}$
	* $R_2 =  \{(a, b): a > b\}$
	* $R_3 = \{(a, b): a = b \vee a = -b\}$
	* $R_4 = \{(a, b): a = b\}$
	* $R_5 = \{(a, b): a = b + 1\}$
	* $R_6 = \{(a, b): a + b \leq 3\}$
* There are a lot of possible relations on a finite set $A$, more specifically, $|\mathcal{P}(A\times A)|$ that many. 
* Notice that, $R_3 = R_4 \cup \{(a, b): a = - b\}$, which is basically $\{(a,b): |a| = |b|\}$

#### Properties of Relations and their Defs
* Reflexive: 
	* $(a, a) \in R \;\forall a \in A$
	* For all vertex in the graph, a self edge exists.
	* $R_1, R_3, R_4$ have this property
* Symmetric
	* $(a, b)\in R \implies (b, a)\in R \; \forall a, b \in A$
	* If there is an edge connecting 2 vertices, then the edge has to be bidirectional.
	* $R_3, R_4, R_5, R_6$ have this property. 
* Antisymmetric
	* $\forall a, b \in A: \; (a, b) \in R \wedge (b, a)\in R \implies a = b$
	* For any pair of vertices in the graph, they cannot share more than 1 edges in common. 
	* $R_1, R_2, R_3, R_4$ have this property. 
	* $R_2$ is true because the quantifier is false at the very beginning, and it's a great example where it's both antisymmetric and symmetric. 
	* This is like a general case of relation. 
	* It's easier to remeber this by negation, if $\exists (a, b), (b, a)\in R \wedge a \neq b$ then the relation is antisymmetric. 
* Transitive
	* $(a, b)\in R \wedge (b, c)\in R \implies (a, c) \in R$
	* The graph is a DAG, excluding the self edges ofc.
	* $R_1, R_2, R_3, R_4$ are transitive relations.


#### More Exmples

* Is the divisble relation on the positive integers, a transitive relations? 
	* $a|b$, $a$ can be divided by $b$, $b|c$, $b$ can be diviced by $c$, and it means the following: 
	* $a = b*m$, $b = c*n$ where $m, n\in \mathbb{N}$, which means $c = mnc$, which means $a|c$. 
	* $R:= \{(a, b): a|b\}$ is a  transitive relation.
* Is the integer divisible relation symmetric, or antisymmetric. 
	* It's not symmetric because: $2\not{|}4$ but $4|2$. 
	* It's antisymmetric, which means that: $a|b\wedge b|a$, which means that $a = mb = mna$, and the only way that the statement can be true is $m = n = 1$ and $a = b$

#### Representation of Relations
* Matrices, boolean matrices
	* $(M_R)_{i, j} = bool((i, j)\in R)$
* Digraph

#### Algebra With Relations
* All the set algebra involving: $\cup$, $\cap$, $\oplus$ and $\setminus$ can be applied to relations
* Relations can be **composed** together. 
	* Def Composition of Relations as the following: 
		* Let $R$ be a relation such that $S$ is on $A\times B$
		* Let $S$ be a relation such that $S$ is on $B\times C$
		* Then the composition relation of $R$ to $S$ is denoted as: $R\circ S$
		* $(a, c) \in R\circ S \iff \exists (a, b)\in R \wedge (b, c)\in S$
		* And that includes all elements in the composite relation.
* Exponential Operations
	* $R^1 = R$, $R^2 = R\circ R$, $R^3 = (R\circ R)\circ R$, and recursively define $R^{n+1} = R^{n}\circ R$
* Note:
	* $\cup, \cap, \oplus$ is just element wise boolean operations on matrices for $S, R$. 
	* Exponetial and composition of relations are literally matrices multiplications on the relational matrix, but all the operations on the field are replaced with boolean operators, unless the results are explicitly not wanted as another boolean matrix. 

---

#### Theorem 1 (Transitivity and Exponential)
* $R$ on $A\times A$ is transitive $\iff$ $R^n\subseteq R\quad \forall\; n\in \mathbb{N}$
	* The proof is by induction and follows directly from the definition of transitivty, super easy. 
#### Theorem 2 (Paths in Graphs)
* Given a digraph $G(V, E)$, define the relations $R$ to contain $(u, v)$ if there eixsts a path starts from $u$ ends with $v$
* Then, there is a path of length $n$ from $u$ to $v$ if and only if $(u, v)\in R^n$ or a walk, if $n$ is larger than $|V|$. 

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
* This is related to one of the graph algorithms for finding the shortest path called "Floyd Warshall's Shortest Path algorithm", [[Graph Algorithms]]


#### Partial Ordering
Def: A Partial Ordering is a relation where it's: 
* Reflexive: $(a, a)\in R \quad \forall a\in A$
* Antisymmetric $(a, b)\in R \wedge (b, a)\in R \implies a = b$
* Transitive $(a, b), (b, c)\in R \implies (a, c)\in R$
#### Total Ordered
* First it has to be a Partial Order
* Every 2 elements in the set is comparable, then $(a, b)$ means $a\prec b$, 
* Another equivalent definition is: 
	* Every Non-empty subsets has a least element. If not, then there eists a subset of $T\subset S$, such that there are 2 elements in $T$ that are not comparable. 

#### Poset
* if, $\exists \; a,b \in R : (a, b)\not\in R \wedge (b,a)\not\in R$ and $R$ is a relation with all above properties of partial ordering, then, the set is called a: **poset**. Those 2 elements are called : *incomparable*

Partial Ordering as a graph: 
* Self edge for each vertex. 
* There is only one directed edge between each pair of vertices in the graph. 
* The graph is a DAG when all self edges are removed. 

##### Examples of Partial Ordering
* $\geq$ with $\mathbb{Z}$
	* Reflexive: Trivial 
	* Antisymmetric: Trivial
	* Transitive: Trivial
* $|$ with $\mathbb{Z}_+$
	* $\forall a \in \mathbb{Z}_+ \;a|a$ is True
	* Assume $(a|b) \wedge (b|a)$ then $a = mb$ and $b = na$ where $m, n \in \mathbb{Z}_+$, which is $a = mnb$ giving us $mn = 1$ hence $a = b$ meaning that the relation is anti-symmetric. 
	* $a|b \wedge b|c$, meaning that $a = bm \wedge b = nc$ where $m, n\in \mathbb{Z}_+$, this will mean that $a = mnc$, and $mn\in \mathbb{Z}_+$, resulting in $a|c$ and then the relation will be transitive. 
	* The relation is not total ordered because there eixsts 2 elements that are not comparable, $4\not{|}\;7$ and $7\not{|}4$
* $\subseteq$ with $\mathcal{P}(S)$ 
	* For this case, we assume that the set $S$  is finite. 

---
### N-ary Relations
* $R$ on $A_1\times A_2\times A_3...\times A_n$, then $R$ is a set tuples with size $n$ where $n$ is going to be called the dimension of the relation. 
	* This is getting close the the territory of Relation Databases.
* A relational database contain a set of tuples, and the tuples are n-ary relation in our context. 
	* (Name, ID, Major, GPA), a 4 dimensional tuple. 
	* **Primary Key**: The domain of the data base, used to distinguish different tuples.
		* Composite Key: Combinations of Domains that unique identify the n-tuples.
	* **Extension**: The current collection of N tuples, (keys might got removed)
	* **Degree**: The length of the tuples in the database.

### Relational Databases
* Operations on relational data bases. 
	* **Selction**: get all tuple satisfying a given predicate.
	* **Projection**: A reduction on tuples
		* $(a_1, a_2... a_n)$ --> $(a_{i1}, a_{i2}, a_{i3}... a_{im})$ , where the sequences $a_{ik}$ is a subsequence of $a_{i}$
		* The above operations is a projection from the $n$ tuples to the $m$ tuples, it's a reduction on the dimension of n-ary.
	* **Join**:
		* This is possible when the keys in the tuples are shared by 2 relations $R$, $S$, let's say $R, S$ are relations of degree $m$ and $n$.
		* More specifically, let's say that the relations are constructed as: 
			* $R = A_1\times A_2\times ... A_{m-p}\times C_1\times C_2\times... C_p$
			* Notice the degree is still m. 
			* $S = C_1\times C_2\times... \times C_p\times B_1\times B_2... \times B_{n-p}$
		* Then, the joined relation will have a size of $m+n - p$, and it will consits of tuples like: $(a_1, a_2...a_{m-p}, c_1, c_2... c_{p},b_1, b_2... b_{n-p})$