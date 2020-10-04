package graph;

public class WeightedEdge extends Edge implements Comparable<WeightedEdge>{

    double Weight;
    public WeightedEdge(int u, int v, double weight) {
        super(u, v);
        Weight = weight;
    }

    @Override
    public int compareTo(WeightedEdge o) {
        return (int) Math.signum(this.Weight - o.Weight);
    }

    /**
     * edges that goes from u to v with different weights are equal, hence, no multiple edges supported
     * for graph using this type of weighted edge.
     * @param o
     * @return
     */
    @Override
    public boolean equals(Object o)
    {
        return super.equals(o);
    }

}
