import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.TreeMap;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.lang.System;

/**
 * 
 *    Keep the median of a stream of integers, in real time.
 *    This is going to be a min max approach.
 *    We are gonna keep the requencies of the elements too
 *    - 
 *      The max of the mean heap is supposed to be the median. 
 * 
 *      [1, 2, 3, 4, 5]  Odd
 * 
 *      [1, 2, 3, 4, 4.5, 5]  Add right
 *      [1, 2, 2.5, 3, 4, 5] add left
 * 
 *      [1, 2, 3, 4, 5, 6] Even
 *
 *      [1, 2, 3, 4, 5, 6, 7] add right
 *      [0, 1, 2, 3, 4, 5, 6] add left
 * 
 *      // Big problme the size of the heap is not elements larger/smaller than the median.
 *      // What if we have [1, 1, 1, 1, 1, 2], then the median got splitted to the min heap and the max heap. 
 */

class MedianKeeper 
{
    public static void main(String[] args)
    {
        {
            System.out.println("Started ... ");
            int[] arr = {3, 4, 1, 2, 5, 6, 7, 9, 0, 8};
            MedianKeeper Keeper = new MedianKeeper();
            for (int I = 0; I < arr.length; I ++)
            {
                Keeper.add(arr[I]);
            }
            System.out.println(Keeper.getMedian());
            Keeper.remove(0);
            System.out.println(Keeper.getMedian());
        }
        // 
        {
            int K = 12;
            List<Integer> RandomShuffled = TestingStuff.getShuffled(1000, 500);
            MedianKeeper Keeper = new MedianKeeper();
            for (int I = 0; I < K; I++)
            {
                Keeper.add(RandomShuffled.get(I));
            }
            for (int I = 0; I < RandomShuffled.size() - K; I++)
            {
                double Median1 = Keeper.getMedian();
                double Median2 = TestingStuff.medianFind(I, I + K, RandomShuffled);
                System.out.println("Median1 is: " + Median1);
                System.out.println("Median2 is: " + Median2);
                if (Median2 != Median1)
                {
                    System.out.println("The answers different");
                    throw new RuntimeException();
                }
                Keeper.remove(RandomShuffled.get(I));
                Keeper.add(RandomShuffled.get(I + K));
            }
        }

    }

    int LessEqualThanMedian = 0, LargerThanMedian = 0; // this will be important to handle the case where : 

    // There are number that repeats multiple times. 
    // The new added number is the median
    TreeMap<Integer, Integer> MinHeap = new TreeMap<>();  // Less than
    TreeMap<Integer, Integer> MaxHeap = new TreeMap<>();  // Greater than

    protected static void removeFromMap(TreeMap<Integer, Integer> theMap, int a)
    {   
        int Freq = theMap.get(a);
        if (Freq == 1)
        {
            theMap.remove(a);
        }
        else
        {
            theMap.put(a, theMap.get(a) - 1);
        }
    }

    protected static void addToMap(TreeMap<Integer, Integer> theMap, int a)
    {

        if (theMap.containsKey(a))
        {
            theMap.put(a, theMap.get(a) + 1);
        }
        else
        {
            theMap.put(a, 1);
        }
    }

    public double getMedian()
    {
        int size = LessEqualThanMedian + LargerThanMedian;
        if (size == 1)return MinHeap.firstKey();
        int M1 = MinHeap.lastKey(), M2 = MaxHeap.firstKey();
        if (size % 2 == 0)
        {
            return (M1 + M2 + 0.0)/2;
        }
        return M1;
    }

    public void add(int a)
    {
    
        int size = LessEqualThanMedian + LargerThanMedian;
        if (size < 2)
        {
            if (size == 0)
            {
                addToMap(MinHeap, a);
                LessEqualThanMedian++;
                return;
            }
            addToMap(MaxHeap, a);
            LargerThanMedian++;
            return;
        }

        int Median = MinHeap.lastKey();
        if (a <= Median)
        {
            if (size % 2 == 0)
            {
                addToMap(MinHeap, a);
                LessEqualThanMedian++;
            }
            else
            {
                removeFromMap(MinHeap, Median);
                LessEqualThanMedian--;
                addToMap(MaxHeap, Median);
                LargerThanMedian++;
                addToMap(MinHeap, a);
                LessEqualThanMedian++;
            }
            return;
        }
        if (a == Median)
        {
            
            // TODO: This
            return;
        }

        if (size %2 == 1)
        {
            addToMap(MaxHeap, a);
            LargerThanMedian++;
        }
        else
        {
            int MaxHeapBottom = MaxHeap.firstKey();
            removeFromMap(MaxHeap, MaxHeapBottom);
            LargerThanMedian--;
            addToMap(MinHeap, MaxHeapBottom);
            LessEqualThanMedian++;
            addToMap(MaxHeap, a);
            LargerThanMedian++;
        }
       
    }

    public void remove(int a)
    {
       
        if (MaxHeap.containsKey(a) || MinHeap.containsKey(a))
        {
            int size = MinHeap.size() + MaxHeap.size();
            int Median = MinHeap.lastKey();
            if (a < Median)
            {
                if (size % 2 == 0)
                {
                    removeFromMap(MinHeap, a);
                    int MaxHeapBottom = MaxHeap.firstKey();
                    addToMap(MinHeap, MaxHeapBottom);
                    removeFromMap(MaxHeap, MaxHeapBottom);
                }
                else
                {
                    removeFromMap(MinHeap, a);
                }
                
                return;
            }
            if (a == Median)
            {   
                // TODO: This
                return;
            }
            // right size
            if (size % 2 == 1)
            {
                removeFromMap(MaxHeap, a);
                int BottomMaxHeap = MaxHeap.firstKey();
                addToMap(MinHeap, BottomMaxHeap);
            }
            else
            {
                removeFromMap(MaxHeap, a);
            }
        }
        else
        {
            throw new IllegalArgumentException("");
        }
    }

}

/**
 * This class is for testing stuff. 
 */
class TestingStuff
{

    public static double medianFind(int i , int j, List<Integer> arr)
    {
        List<Integer> Section = IntStream.range(i, j)
        .mapToObj
        ((k) -> arr.get(k)).collect(Collectors.toList());
        Collections.sort(Section);
        int Size = Section.size();
        double M1 = Section.get(Size/2 - 1), M2 = Section.get(Size/2);
        return Size % 2 == 0? (M1 + M2 + 0.0)/2: M2;
    }

    public static List<Integer> getShuffled(int n, int maxElement)
    {
        List<Integer> Ans = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            Ans.add((int)(Math.random()*maxElement));
        }
        Collections.shuffle(Ans);
        return Ans;
    }

}