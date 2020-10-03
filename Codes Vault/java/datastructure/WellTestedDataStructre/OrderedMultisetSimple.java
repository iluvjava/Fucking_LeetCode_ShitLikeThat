package datastructure.WellTestedDataStructre;

import java.util.List;
import java.util.TreeMap;
import java.util.stream.Collectors;

/**
 * 
 * This class deal with a multiset, it aims to improve speed when there are a lot of multiples of the 
 * same elements in the sequence.
 *   Features: 
 *   * Get the max element
 *   * get the min element
 *   * Get the number of elements, (counting the repeating)
 *   * Remove element one by one
 *   * Add element one by one, or in bulk. 
 */
public class OrderedMultisetSimple<T extends Comparable> {

    protected TreeMap<T, Integer> FreqTable;
    protected int Size = 0;

    public OrderedMultisetSimple()
    {
        FreqTable = new TreeMap<>();
    }

    public OrderedMultisetSimple(List<T> sequence)
    {
        FreqTable = sequence
                            .stream()
                            .collect(
                                Collectors.groupingBy(
                                    (e) -> e, 
                                    TreeMap::new,
                                    Collectors.summingInt(e-> 1)
                                )
                        );
    }

    public int size()
    {
        return Size;
    }

    public void add(T e)
    {
       FreqTable.put(e, FreqTable.getOrDefault(e, 0) + 1);
       Size++ ;
    }

    public void add(T... e)
    {
        for (T item :e)
        {
            add(item);
        }
    }

    public boolean contains(T e)
    {
        return FreqTable.containsKey(e);
    }

    public void remove(T e)
    {
        if (!FreqTable.containsKey(e)) throw new RuntimeException();
        if (FreqTable.get(e) == 1)
        {
            FreqTable.remove(e);
        }
        else
        {
            FreqTable.put(e, FreqTable.get(e) - 1);
        }
        Size--;
    }

    public int frequencyOf(T e)
    {
        return 0;
    }

    public T getMax()
    {
        return FreqTable.lastKey();
    }

    public T getMin()
    {
        return FreqTable.firstKey();
    }

    @Override
    public String toString()
    {
        return FreqTable.toString();
    }


}