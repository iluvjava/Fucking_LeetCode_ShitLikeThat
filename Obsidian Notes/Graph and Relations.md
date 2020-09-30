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
	* Given a matrix representation of the transitive relation of $R$, say $M$, we can use the boolean matrix to compute the transitive closure of the graph, simply by doing: $\bigvee_{k = 1}^n M^k$

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