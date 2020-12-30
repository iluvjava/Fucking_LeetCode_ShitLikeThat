## Intro
Def a graph is: $G(V, E)$, a set of vertices and a set of edges, where the set of edges are $E= \{(a, b): a, b \in V\}$, the edges are relations on $V$. 

------------------

* More algorithms and computer science related: [[Graph Algorithms]]
* Something more mathy and abstract: [[Graph and Relations]]


### Graph Metric (Distance)

Yes, it's the metric space for a graph

The distance function forms a metric space for any given graph if and only if the graph is a connected graph. 

#### Eccentricity

The Eccentricity of a vertex is the greatest distance from that vertex to all other vertices on the graph. 

Let the distance function of 2 vertex be $d(u, v)$ where it returns the length of the shortest path going between the vertex $u, v$. 

> $$\epsilon(v) = \max_{u\in V} d(v, u)$$


#### Diameter

* The diameter of a graph is the maximal eccentricity of the graph. It's asking the question, what is the maximal shortest distance among all possible pair of vertices in the graph? 

> $$\max_{v\in V}(\epsilon(v))$$

* The vertex of the largest eccentricity is called the **peripheral vertex**. 

#### Radius

* The radius of the graph is the minimal eccentricity, it's asking the question, among all possible pairs of vertices on the graph, what could be the shortest distance? 

> $$\min_{v\in V} (\epsilon(v))$$

* The vertex with such an eccentricity is called the **Central Vertex**. 