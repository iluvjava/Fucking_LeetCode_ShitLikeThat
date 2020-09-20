import java.until.Arrays;
import java.lang.Math;
class Solution {

    public static void main(string[] args)
    {
        
    }

    public static int solution(int[] arg)
    {
        Arrays.sort(arg);
        int Maxabs = Integer.Max_VALUE;
        for (int I = 1; I < arg.length; I++)
        {
            Maxabs = Math.min(Maxabs, Math.abs(arg[I] - arg[I - 1]));
        }
        return Maxabs;
    }

}