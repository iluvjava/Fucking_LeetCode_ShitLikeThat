Partial Order, Total Order of a relation

---

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


