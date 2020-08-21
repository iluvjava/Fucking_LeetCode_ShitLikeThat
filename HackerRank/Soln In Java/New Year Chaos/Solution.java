import java.lang.System;
import java.lang.Math;

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

        int TotalBribes = 0;
        for (int I = 1; I < n; I++)
        {
            for (int J = 0; J < I; J++)
            {
                if (q[J] > q[I])TotalBribes++;
            }
        }
        return TotalBribes;
    }
}
