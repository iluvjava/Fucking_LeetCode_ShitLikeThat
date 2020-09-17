import java.lang.System;
import java.util.*;

class Solution
{
    public static void main(String[] args)
    {
        int[][] Query = {
            new int[] {2, 6, 8}, 
            new int[] {3, 5, 7}, 
            new int[] {1, 8, 1}, 
            new int[] {5, 9, 15}
        };
        System.out.print(arrayManipulation(100, Query));
    }

    // Complete the arrayManipulation function below.
    static long arrayManipulation(int n, int[][] queries) {
        // Input parameter n is not that useful. 
        
        TreeMap<Integer, Integer> BoundaryValue = new TreeMap<>();
        {
            for (int[] Triplet : queries)
            {
                BoundaryValue.put(Triplet[0], Triplet[2] +
                    BoundaryValue.getOrDefault(Triplet[0], 0)
                );
                BoundaryValue.put(Triplet[1] + 1, - Triplet[2] + 
                    BoundaryValue.getOrDefault(Triplet[1] + 1, 0)
                );
            }
        }
        System.out.println("Countructed Boundary Value: ");
        System.out.println(BoundaryValue);

        long RunningSum = 0;
        long MaxRunningSum = 0;
        for (Map.Entry<Integer, Integer> Kvp : BoundaryValue.entrySet())
        {
            RunningSum += Kvp.getValue();
            MaxRunningSum = Math.max(RunningSum, MaxRunningSum);
        }
        return MaxRunningSum;

    }


}