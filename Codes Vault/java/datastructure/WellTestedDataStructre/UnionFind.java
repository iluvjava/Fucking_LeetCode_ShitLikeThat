package datastructure.WellTestedDataStructre;
import java.util.HashMap;
import java.util.Map;


/**
 * Union find with path conpression but without the tree ranking. The
 * representative will be anchored when joing 2 elements in the data structure.
 * 
 * * Self loop is the root of the tree. 
 */
public class UnionFind<T> {

    public static void main(String[] args)
    {

    }


    Map<T, T> Forest = new HashMap<>();

    /**
     * Add a new element to the UnionFind data structure. 
     * @param element
     */
    public void add(T element)
    {
        Forest.put(element, element);
    }
    
    /**
     * Join 2 of the element to one group, with a's representative representing the group for b.
     * @param a
     * @param b
     */
    public void join(T a, T b)
    {
        T ReprA = get(a);
        T ReprB = get(b);
        Forest.put(ReprA, ReprB);
        return;
    }

    /**
     * Get the representative of the given element. 
     * @param element
     * @return
     */
    public T get(T element)
    {
        if (Forest.get(element) == element)
        {
            return element;
        }
        T ElementRepresent = get(Forest.get(element));
        Forest.put(element, ElementRepresent);
        return ElementRepresent;
    }
}
