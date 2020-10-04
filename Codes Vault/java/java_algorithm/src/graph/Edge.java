package graph;

import java.util.Objects;

/**
 * Link u --> v
 */
public class Edge{
    protected final int v, u;

    public Edge(int u, int v)
    {
        this.u = u;
        this.v = v;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Edge edge = (Edge) o;
        return v == edge.v &&
                u == edge.u;
    }

    @Override
    public int hashCode() {
        return Objects.hash(v, u);
    }
}
