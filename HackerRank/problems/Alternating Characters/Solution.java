import java.util.*;
import java.lang.System;
class Solution
{

    public static void main(String[] args)
    {
        System.out.println(MinimumDeletion("AAABBB"));
    }

    public static int MinimumDeletion(String s)
    {
        int MinimumDeletions = 0;
        {
            Stack<Character> TheStack = new Stack<>();
            for(char C : s.toCharArray())
            {
                if (TheStack.size() == 0 || TheStack.peek() != C)
                {
                    TheStack.add(C);
                }
                else
                {
                    MinimumDeletions += 1;
                }
            }
        }
        return MinimumDeletions;

    }

}