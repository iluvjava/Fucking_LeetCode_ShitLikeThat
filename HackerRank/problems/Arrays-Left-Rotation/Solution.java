import java.util.Arrays;
import java.lang.System;

/**
 * This is a failed solution and it actually doesn't work.
 */
class Soluiton {
    
    public static void main(String[] args)
    {
        solution(new int[]{0, 1, 2, 3}, 2);
        solution(new int[]{0, 1, 2, 3}, 3);
        solution(new int[]{0, 1, 2, 3, 4}, 2);
        solution(new int[]{0, 1, 2, 3, 4}, 3);
        solution(new int[]{0, 1, 2, 3, 4}, 4);
        solution(new int[]{0, 1, 2, 3, 4, 5, 6, 7}, 3);
    }

    /**
     * 
     * @param a
     * @param d
     * @return
     */
    public static int[] solution(int[] a, int d)
    {
        int[] Aux = new int[a.length];
        {
            int I = 0;
            for (int J = d; J < a.length; I++, J++)
            {
                Aux[I] = a[J];
            }
            int J = 0;
            while (I < a.length)
            {
                Aux[I++] = a[J++];
            }
        }
        System.out.println(Arrays.toString(Aux));
        return Aux;
    }

    /**
     * This is an failed attempt, forget about it. 
     * @param a
     * @param d
     * @return
     */
    static int[] rotLeft(int[] a, int d) 
    {
        boolean Left2Right = d <= a.length/2;
        if (!Left2Right) d = a.length - d;
        int I = Left2Right? 0: a.length - 1 - d;
        int J = Left2Right? d: a.length - 1;
        
        while(0 <= I && J < a.length && 0 <= J && J<= a.length)
        {
            int Temp = a[J]; 
            a[J] = a[I];
            a[I] = Temp;
            if (Left2Right) 
            {
                I++; J++;
            }
            else
            {
                I--; J--;
            }
        }
        if (a.length%2 == 1 && d - 1 == a.length/2)
        {
            int Temp = a[J]; 
            a[J] = a[I];
            a[I] = Temp;
        }

        System.out.println(Arrays.toString(a));
        return a;
    }

}