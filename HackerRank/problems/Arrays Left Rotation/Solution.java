import java.util.Arrays;
import java.lang.System;

/**
 * This is a failed solution and it actually doesn't work.
 */
class Soluiton {
    
    public static void main(String[] args)
    {
        rotLeft(new int[]{0, 1, 2, 3}, 2);
        rotLeft(new int[]{0, 1, 2, 3}, 3);
        rotLeft(new int[]{0, 1, 2, 3, 4}, 2);
        rotLeft(new int[]{0, 1, 2, 3, 4}, 3);
        rotLeft(new int[]{0, 1, 2, 3, 4}, 4);
        rotLeft(new int[]{0, 1, 2, 3, 4, 5, 6, 7}, 3);
    }

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