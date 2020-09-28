import java.util.Arrays;

class Solution
{

    public static void main(String[] args)
    {
        System.out.println("It's Running...");
        // System.out.println(MinLenSubstring("-ab--c-", "abc"));
        // System.out.println(MinLenSubstring("a-cb-a-c--bc", "abc"));
        System.out.println(MinLenSubstring("m-m", "mm"));
    }

    public static String MinLenSubstring(String s, String t)
    {
        // J: index for "s", I: Index for "t"
        int[] DP = new int[t.length()];
        {   
            // Initialization
            DP[0] = t.charAt(0) == s.charAt(0)? 0 : -1;
            for (int I = 1; I < t.length(); I++)
            {
                DP[I] = -1;
            }
            System.out.println("Initialization of the array: ");
            System.out.println(Arrays.toString(DP));
        }
        int MinWindowLeft = -1;
        int MinWindowRight = -1;
        {
            int MinWindowLen = Integer.MAX_VALUE;
            for (int J = 1; J < s.length(); J++)
            {
                int[] NewDP = new int[t.length()];
                NewDP[0] = s.charAt(J) == t.charAt(0)? J: DP[0];
                for (int I = 1; I < t.length(); I ++)
                {
                    NewDP[I] = s.charAt(J) == t.charAt(I)? DP[I - 1]: DP[I];
                }
                System.out.println(Arrays.toString(NewDP));
                DP = NewDP;
                if (DP[DP.length - 1] != -1)
                {
                    int LeftWinIndex = DP[DP.length - 1];
                    if (J - LeftWinIndex < MinWindowLen)
                    {
                        MinWindowLen = J - LeftWinIndex;
                        MinWindowLeft = LeftWinIndex;
                        MinWindowRight = J;
                    }
                }
            }
        }
        if (MinWindowLeft == -1) return "";
        return s.substring(MinWindowLeft, MinWindowRight + 1);
    }


}