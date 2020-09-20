import java.lang.System;
class Solution {

    public static void main(String[] args)
    {
        System.out.println(solution(new int[]{7, 1, 3, 2, 4, 5, 6}));        
    }


    public static int solution(int[] graph) 
    {
        int[] Visited = new int[graph.length];  // 1: visited
        int Res = 0;
        for (int StartPoint = 0; StartPoint < graph.length; StartPoint++)
        {
            if (Visited[StartPoint] == 1) continue;
            Visited[StartPoint] = 1;
            int Pointer = graph[StartPoint] - 1;
            while (Pointer != StartPoint)
            {
                Visited[Pointer] = 1;
                Pointer = graph[Pointer] - 1;
                Res++;
            }
        }
        return Res;
    }

}