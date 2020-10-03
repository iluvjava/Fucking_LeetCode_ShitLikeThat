package WellTestedDataStructure;
import java.util.TreeMap;

class MedianKeeper
{
    protected int Larger;
    protected int LessThanOrEqual;
    protected TreeMap<Integer, Integer> Min = new TreeMap<>();
    protected TreeMap<Integer, Integer> Max = new TreeMap<>();
     
    public double getMedian()
    {
        int Size = Larger + LessThanOrEqual;
        if (Larger + LessThanOrEqual == 1)
        {
            return Min.lastKey();
        }
        long M1 = Min.lastKey(), M2 = Max.firstKey();
        return Size % 2 == 0? (M1 + M2 + 0.0)/2 : M1;
    }


    public void add (int a)
    {
        int Total = Larger + LessThanOrEqual;
    
        if (Total == 0)
        {
            addToMin(a);
            return;
        }
        else
        {
            int MinTop = Min.lastKey();
            if (a > MinTop)
            {
                addToMax(a);
            }
            else
            {
                addToMin(a);    
            }
        }
        balanceItself();
    }

    protected void balanceItself()
    {
        int Total = LessThanOrEqual + Larger;
        
        while (LessThanOrEqual - (Total % 2) != Larger)
        {
            if (LessThanOrEqual - (Total % 2) > Larger)
            {
                int ToMove = Min.lastKey();
                removeFromMin(ToMove);
                addToMax(ToMove);
            }
            else
            {
                int ToMove = Max.firstKey();
                removeFromMax(ToMove);
                addToMin(ToMove);
            }
        }
    }

    public void remove(int a)
    {
        if (Min.containsKey(a))
        {
            removeFromMin(a);
            balanceItself();
            return;
        }
        
        if (Max.containsKey(a))
        {
            removeFromMax(a);
            balanceItself();
            return;
        }
        throw new IllegalArgumentException("Can't remove something that is not present");
    }

    protected void addToMin(int a)
    {
        addToMap(Min, a);
        LessThanOrEqual++;
    }

    protected void addToMax(int a)
    {
        addToMap(Max, a);
        Larger++;
    }

    protected void removeFromMin(int a)
    {
        removeFromMap(Min, a);
        LessThanOrEqual--;
    }

    protected void removeFromMax(int a)
    {
        removeFromMap(Max, a);
        Larger--;
    }

    public static<T> void addToMap(TreeMap<T, Integer> treeMap, T stuffToAdd)
    {
        if (treeMap.containsKey(stuffToAdd))
        {
            treeMap.put(stuffToAdd, treeMap.get(stuffToAdd) + 1);
        }
        else
        {
            treeMap.put(stuffToAdd, 1);
        }
    }

    public static <T> void removeFromMap(TreeMap<T, Integer> treeMap, T stuffToRemove)
    {
        if (treeMap.get(stuffToRemove) == 1)
        {
            treeMap.remove(stuffToRemove);
        }
        else
        {
            treeMap.put(stuffToRemove, treeMap.get(stuffToRemove) - 1);
        }

    }

    public String toString()
    {
        StringBuilder Sb = new StringBuilder();
        Sb.append(Min.toString());
        Sb.append("\n");
        Sb.append(Max.toString());
        return Sb.toString();
    }

}