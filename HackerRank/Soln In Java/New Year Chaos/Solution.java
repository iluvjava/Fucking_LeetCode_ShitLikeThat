import java.lang.System;
import java.lang.Math;
import java.util.Arrays;


class Solution {

    public static void main(String[] args)
    {
        int[] Test1 = new int[]{2, 1, 5, 3, 4};  // 3,
        int[] Test2 = new int[]{2, 5, 1, 3, 4};  // -1
        int[] Test3 = new int[]{5, 1, 2, 3, 7, 8, 6, 4};  // -1
        int[] Test4 = new int[]{1, 2, 5, 3, 7, 8, 6, 4};  // 7


        System.out.println(solution(Test1));
        System.out.println(solution(Test2));
        System.out.println(solution(Test3));
        System.out.println(solution(Test4));
        // can't use the test cases anymore cause they are modified. 
        System.out.println(countInversion(new int[]{8, 7, 6, 5, 4, 3, 2, 1}));
    }

    /**
     *  -1 means TO Chaotic, else it's the minum number of bribes needed to 
     * achieve that configuration. 
     * @param q
     * @return
     */
    public static int solution(int[] q)
    {
        int n = q.length;
        int MaxLeftInversion = 0;
        for (int I = 0; I < n; I++)
        {
            if (q[I] - (I + 1) > 0)
                MaxLeftInversion = Math.max(q[I] - (I + 1), MaxLeftInversion);
        }
        if (MaxLeftInversion > 2) return - 1; 
        
        return countInversion(q);
    }

    
    public static int countInversion(int[] arr)
    {
        int[] backup = Arrays.copyOf(arr, arr.length);
        return countInversion(backup, 0, arr.length, new int[arr.length]);
    }
    /**
     * left inclusive, right exclusive. 
     * Mutable and array is modified.  
     * @return
     */
    private static int countInversion(int[] arr,  int start, int end, int[] buckets)
    {
        // basecase, length of sub array is <= 2; 
        if (end - start <= 2)
        {
            if (end - start == 2)
            {
                if (arr[start] <= arr[end - 1])
                {
                    return 0;
                }
                else
                {
                    int temp = arr[start]; 
                    arr[start] = arr[end - 1];
                    arr[end - 1] = temp;
                    return 1;
                }
            }
            return 0;
        }
        int Mid = (start + end)/2; // left: start <= I < mid; right: mid <= J < end 
        int LeftInversions = countInversion(arr, start, Mid, buckets); 
        int RightInverions = countInversion(arr, Mid, end, buckets);
        int MergeInverions = 0;
        {
            int I = start, J = Mid, K = 0; // K: offset from: "start position"
            while(I < Mid && J < end)
            {
                if(arr[I] <= arr[J])
                {
                    buckets[start + (K++)] = arr[I];
                    I++;
                }
                else
                {
                    buckets[start + (K++)] = arr[J];
                    MergeInverions += Mid - I;
                    J++;
                }
            }
            while(I < Mid || J < end)
            {
                if (I < Mid) buckets[K++] = arr[I++];
                if (J < end) buckets[K++] = arr[J++];
            }
        }
        for (int I = start; I < end; I++)
        {
            arr[I] = buckets[I];
        }
        return LeftInversions + RightInverions + MergeInverions;
    }

    
}

class TestThatShit
{

}
