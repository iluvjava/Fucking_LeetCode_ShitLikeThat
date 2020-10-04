package graph;


import java.util.*;

/**
 * Goal:
 *    * This class is modeling all vertex with integer
 *    * This emulates the implementation advantages from both the Adjlist list implementations and
 *    the matrix implementations
 * Features:
 *    * Associate vertex to it's out coming edges in sorted order
 *    * Store all the edges in sorted order
 *    * Easy indexing with tuples to find the weight of the edges
 */
public class WeightedDigraph extends Digraph {

    protected Map<Edge, WeightedEdge> EdgeToWeight;
    protected Map<Integer, SortedSet<WeightedEdge>> OutGoingEdges;
    protected Map<Integer, SortedSet<WeightedEdge>> IncomingEdges;

    public WeightedDigraph()
    {
        EdgeToWeight = new HashMap<>();
        OutGoingEdges = new TreeMap<>();
        IncomingEdges = new TreeMap<>();
    }






}
