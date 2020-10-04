package graph;
import java.util.*;

/**
 * This class is attempting to model a simple digraph.
 *   * The edges and the vertices are just integers, strictly ranging from 1 to N
 *   * Multi directed edges both going from u to v is not supported.
 *
 */
public class Digraph
{

    protected Map<Integer, SortedSet<Integer>> OutGoingEdges = new HashMap<>();
    protected Map<Integer, SortedSet<Integer>> IncomingEdges = new TreeMap<>();

    protected int Vsize = 0;

    public Digraph()
    {
        // Default constructor.
    }

    /**
     * creates a fix number of isolated vertices in the graph.
     * @param size
     */
    public Digraph(int size)
    {
        for (int I = 0; I < size; I++) addVertex();
    }

    public void addVertex()
    {
        OutGoingEdges.put(Vsize++, new TreeSet<>());
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
            SortedSet<Integer> NeighboursU = OutGoingEdges.get(u);
            SortedSet<Integer> NeighboursV = IncomingEdges.get(v);
            NeighboursU.add(v);
            NeighboursV.add(u);
        }
    }

    public boolean hasEdge(int v, int u)
    {
        if (!OutGoingEdges.containsKey(v)) return false;
        SortedSet<Integer> Neighbours = OutGoingEdges.get(v);
        return Neighbours.contains(u);
    }

    /**
     *    The neighbours that this vertex points to.
     *    Neighours are sorted by their assigned index.
     * @param vertex
     *    The index of the vertex you want to get.
     * @return
     *    null if the vertex is not part of the graph.
     */
    public Iterator<Integer> getNeighboursPlus(int vertex)
    {
        if (!OutGoingEdges.containsKey(vertex)) return null;
        return OutGoingEdges.get(vertex).iterator();
    }

    /**
     * Neighbours that points to this vertex. Sorted by their integer reprsentative.
     * @param vertex
     * @return
     * null if the vertex is never part of the graph.
     */
    public Iterator<Integer> getneighboursMinus(int vertex)
    {
        if (!IncomingEdges.containsKey(vertex)) return null;
        return IncomingEdges.get(vertex).iterator();
    }


    public int degOut(int u)
    {
        return OutGoingEdges.get(u).size();
    }

    public int degIn(int u)
    {
        return IncomingEdges.get(u).size();
    }

}


