package graph;


import java.util.*;

/**
 * This class is attempting to model a simple digraph.
 *   * The edges and the vertices are just integers, strictly ranging from 1 to N
 *
 */
public class Digraph
{

    protected Map<Integer, SortedSet<Integer>> AdjList  = new HashMap<>();
    protected int Vsize = 0;

    public void addVertex()
    {

    }

    public void addEdges(int v, int u)
    {

    }

    public boolean hasEdge(int v, int u)
    {
        return false;
    }

    public Enumeration<Integer> getNeighbours(int vertex)
    {
        return null;
    }

}


