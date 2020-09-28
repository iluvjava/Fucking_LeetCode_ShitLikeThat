
import java.util.List;
import java.util.TreeMap;
import java.util.stream.Collectors;
import java.lang.Math;


class Solution {

    public static void main(String[] args)
    {
        int[] arr = new int[]{4, 2, 2, 2, 0, 4, 4, 2, 2};
        System.out.println(LongestAbsDiffSubArray(arr, 0));
    }
    
    public static int LongestAbsDiffSubArray(int[] arr, int limit)
    {
        if (arr.length == 1)return 1;
        int MaxSubArraylen = Integer.MIN_VALUE;  // the ans
        {
            OrderedMultisetSimple<Integer> MultiSet = new OrderedMultisetSimple<>();
            MultiSet.add(arr[0]);
            int WindowLeft = 0;
            for (int I = 1; I < arr.length; I++)
            {
                MultiSet.add(arr[I]);
                Integer Min = MultiSet.getMin();
                Integer Max = MultiSet.getMax();
                while (Max - Min > limit && MultiSet.size() > 2)
                {
                    MultiSet.remove(arr[WindowLeft++]);
                    Min = MultiSet.getMin();
                    Max = MultiSet.getMax();
                }
                if (Max - Min <= limit)
                {
                    MaxSubArraylen = Math.max(MaxSubArraylen,  MultiSet.size());
                }
            }
        }
        return MaxSubArraylen;
    }

}

class OrderedMultisetSimple<T extends Comparable> {

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