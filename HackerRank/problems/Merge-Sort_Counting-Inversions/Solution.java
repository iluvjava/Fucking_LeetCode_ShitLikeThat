import java.util.Arrays;

class Solution 
{

    public static void main(String[] args)
    {

    }
    public static long countInversion(int[] arr)
    {
        return countInversion(arr, 0, arr.length, new int[arr.length]);
    }
    
    /**
     * left inclusive, right exclusive. 
     * Mutable and array is modified.  
     * @return
     */
    private static long countInversion(int[] arr,  int start, int end, int[] buckets)
    {
        // basecase, length of sub array is <= 2; 
        if (end - start <= 2)
        {
            if (end - start == 1) return 0;
            else
            {
                if (arr[start] <= arr[end - 1])
                {
                    return 0;
                }
               
                int temp = arr[start]; 
                arr[start] = arr[end - 1];
                arr[end - 1] = temp;
                return 1;
                
            }
        }
        int Mid = (start + end)/2 + 1; // left: start <= I < mid; right: mid <= J < end 
        long LeftInversions = countInversion(arr, start, Mid, buckets); 
        long RightInverions = countInversion(arr, Mid, end, buckets);
        long MergeInverions = 0;
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
                if (I < Mid) buckets[start + (K++)] = arr[I++];
                if (J < end) buckets[start + (K++)] = arr[J++];
            }
        }
        for (int I = start; I < end; I++)
        {
            arr[I] = buckets[I];
        }
        return LeftInversions + RightInverions + MergeInverions;
    }

}