package graph;
import java.util.*;

/**
 * Goal:
 *    * This class is modeling all vertex with integer
 *    * This emulates the implementation advantages from both the Adjlist list implementations and
 *    the matrix implementations
 *    * Everything coming in and coming out of ther API methods of the classes are going to be simple
 *    integers and tuples of integers.
 * Features:
 *    * Associate vertex to it's out coming edges in sorted order
 *    * Store all the edges in sorted order
 *    * Easy indexing with tuples to find the weight of the edges
 * Not A Feature:
 *    * Multiple edges going from u to v.
 */
public class WeightedDigraph extends Digraph {

    protected Map<Edge, WeightedEdge> EdgeToWeight;
    protected Map<Integer, SortedSet<WeightedEdge>> OutGoingEdges;
    protected Map<Integer, SortedSet<WeightedEdge>> IncomingEdges;

    public WeightedDigraph()
    {
        this(0);
    }


    /**
     * Construct a graoh
     * @param size
     * How many vertex you want to start with. (Vertices are all isolated at the beginning)
     */
    public WeightedDigraph(int size)
    {
        super(size);
        EdgeToWeight = new HashMap<>();
        OutGoingEdges = new TreeMap<>();
        IncomingEdges = new TreeMap<>();
    }

    @Override
    public void addVertex() {
        super.addVertex();
        OutGoingEdges.put(Vsize - 1, new TreeSet<>());
        IncomingEdges.put(Vsize - 1, new TreeSet<>());
    }


    /**
     * If no weights specified then the weights are set to 1 by default, nothing will be done
     * if any of the vertices are not in the graph.
     *
     * @param v
     * @param u
     * @return
     * Nothing
     */
    @Override
    public void addEdge(int v, int u) {
        super.addEdge(v, u);
        assignWeightfor(u, v, 1);
    }

    /**
     * <p>
     *      Adds the weight to an edge on the graph. Nothing will be done if the edge doesn't exist
     *      in the graoh.
     * </p>
     * <p>
     *      Returns a list of tuples, sorted in ascending order of the edge weights.
     * </p>
     *
     * @param u
     * @param v
     * @param weight
     *
     */
    public void assignWeightfor(int u, int v, int weight)
    {
        if (v < Vsize && u < Vsize)
        {
            WeightedEdge WeightedEdge = new WeightedEdge(u, v, weight);
            EdgeToWeight.put(new Edge(u, v), WeightedEdge);
            SortedSet<WeightedEdge> EdgesFromU = OutGoingEdges.get(u);
            SortedSet<WeightedEdge> EdgesToV = IncomingEdges.get(v);
            EdgesFromU.add(WeightedEdge);
            EdgesToV.add(WeightedEdge);
        }
    }

    public Iterator<WeightedEdge> getOutgoingWeightedEdges(int u)
    {
        return OutGoingEdges.get(u).iterator();
    }




}
