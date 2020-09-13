import java.lang.System;
class Solution
{

    public static void main(String[] args)
    {
        System.out.println(solution("HARRY", "SALLY"));
        System.out.println(solution("SHINCHAN", "NOHARAAA"));
        System.out.println(solution("ABCDEF", "FBDAMN"));
    }

    public static int solution(String s1, String s2)
    {
        int[] T = new int[s2.length() + 1];
        for (int I = 0; I < s1.length(); I++)
        {
            int[] Tnew = new int[s2.length() + 1];
            for (int J = 0; J < s2.length(); J++)
            {
                if (s1.charAt(I) == s2.charAt(J))
                {
                    Tnew[J + 1] = T[J] + 1;
                }
                else
                {
                    Tnew[J + 1] = Math.max(T[J + 1], Tnew[J]);
                }
            }
            T = Tnew;
        }
        return T[s2.length()];
    }
}