import java.util.*;
import java.lang.System;
class Solution {

    public static void main(String[] args)
    {

        int[] TestArray1 = {1,
                            2,
                            3,
                            4,
                            10,
                            20,
                            30,
                            40,

                            100,
                            200};
        int Res1 = solution(4, TestArray1);
        System.out.println(Res1);
    }


    public static int solution(int k, int[] arr)
    {
        
        Arrays.sort(arr);
        PriorityQueue<Integer> MaxPq = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> MinPq = new PriorityQueue<>();
        for (int I = 0; I < k; I++)
        {
            MaxPq.add(arr[I]);
            MinPq.add(arr[I]);
        }
        int MinUnfairness = MaxPq.peek() - MinPq.peek();
        for (int I = k; I < arr.length; I++)
        {
            MaxPq.remove(arr[I - k]);
            MinPq.remove(arr[I - k]);
            MaxPq.add(arr[I]);
            MinPq.add(arr[I]);
            MinUnfairness = Math.min(MinUnfairness, MaxPq.peek() - MinPq.peek());
        }

        return MinUnfairness;
    }

}