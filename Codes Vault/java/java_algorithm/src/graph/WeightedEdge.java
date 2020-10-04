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

    @Override
    public boolean equals(Object o)
    {
        if (!super.equals(o))return false;
        WeightedEdge OtherEdge = (WeightedEdge) o;
        return OtherEdge.Weight == Weight;
    }

}
