import java.util.Iterator;

import java.util.*;

/**
 * A multi set is a set that supports repeating elements. 
 * 
 */
public class OrderedMultiSet<T extends Comparable> implements Iterable<T> {

    public static void main(String[] args)
    {


    }

    /**
     * Construct the instance from a list of sequences. 
     * @param sequence
     */
    public OrderedMultiSet(List<T> sequence)
    {

    }

    @Override
    public Iterator<T> iterator() {
        // TODO Auto-generated method stub

        return null;
    }


    /**
     * Build a Counter object (the one in python) for any generic 
     * sequence of objects. 
     * @param <T2>
     * @param sequence
     * @return
     * 
     */
    public static <T2> Map<T2, Integer> counterBuild(List<T2> sequence)
    {

        return null;
    } 
    
}
