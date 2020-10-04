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

    public Digraph()
    {

    }

    public Digraph(int size)
    {
        for (int I = 0; I < size; I++)addVertex();
    }

    public void addVertex()
    {
        AdjList.put(Vsize++, new TreeSet<>());
    }

    /**
     * If any of the vertices doesn't exist then it won't do anything.
     * @param u
     *  Integer under the vertex count,
     * @param v
     *  Integer under the vertex count
     */
    public void addEdge(int u, int v)
    {
        if (u < Vsize && u < Vsize)
        {
            SortedSet<Integer> Neighbours = AdjList.get(u);
            Neighbours.add(v);
        }
    }

    public boolean hasEdge(int v, int u)
    {
        if (!AdjList.containsKey(v)) return false;
        SortedSet<Integer> Neighbours = AdjList.get(v);
        return Neighbours.contains(u);
    }

    public Iterator<Integer> getNeighbours(int vertex)
    {
        return AdjList.get(vertex).iterator();
    }

}


