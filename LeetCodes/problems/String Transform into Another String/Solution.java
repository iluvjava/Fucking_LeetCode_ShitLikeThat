import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;



public class Solution {
    
    public static void main(String[] args)
    {
        System.out.println("This shit is running");
        System.out.println(transformPossible("ccdee", "aabcc"));
        System.out.println(transformPossible("leetcode", "codeleet"));
        System.out.println(transformPossible("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"));
        System.out.println(transformPossible("abcdefghijklmnopqrstuvwxyz", "zabcdefghijklmnopqrstuvwxy"));

    }

    public static boolean transformPossible(String s, String t)
    {
        // Simple cases: 
        if (s.equals(t)) return true;
        if (s.length() != t.length()) return false;

        // Complicated cases: 
        TupleStringModel Model1 = new TupleStringModel(s), Model2 = new TupleStringModel(t);
        int[][] Pattern1 = Model1.reduceToPattern();
        int[][] Pattern2 = Model2.reduceToPattern();
        // System.out.println("Patterns:");
        // System.out.println(Arrays.deepToString(Pattern1));
        // System.out.println(Arrays.deepToString(Pattern2));

        if (Pattern2[0].length != Pattern2[0].length) return false;
        for(int I = 0; I < Pattern1[0].length; I++)
        {
            if (Pattern1[0][I] != Pattern2[0][I])return false;
            if (Pattern1[1][I] != Pattern2[1][I])return false;
        }
        if (Model1.uniqueCharactersCount() == 26 && Model2.uniqueCharactersCount() == 26)
        {
            return false;
        }
        return true;
    }

   

}

/**
 * This is a special type of data structure that is creted to solve this problem, hopefully it get use 
 * for other problems in the future too.
 *     * Only suitable for string with lowercased english letters. 
 */
final class TupleStringModel
{
    public final String TheString; 
    protected List<Character> GroupedCharList = new ArrayList<>(); 
    protected List<Integer> GroupedFreqList = new ArrayList<>();

    public TupleStringModel(String s)
    {
        TheString = s;
        StringReduce();
    }

    public int uniqueCharactersCount()
    {
        return GroupedCharList.size();
    }

    public void StringReduce()
    {
        int Counter = 1;
        for (Character C : TheString.toCharArray())
        {
            if
            (
                GroupedCharList.isEmpty()
                ||
                GroupedCharList.get(GroupedCharList.size() - 1)!= C
            )
            {
                GroupedCharList.add(C);
                GroupedFreqList.add(1);
                Counter = 1;
            }
            else
            {
                GroupedFreqList.remove(GroupedFreqList.size() - 1);
                GroupedFreqList.add(++Counter);
            }
        }
    }

    public int[][] reduceToPattern()
    {
        int[] Ids = new int[27];
        {
            Arrays.fill(Ids, -1);
            int Counter = 0;
            for (char C: GroupedCharList)
            {   
                if (Ids[C - 'a'] == -1)Ids[C - 'a'] = Counter++;
            }
        }
        int[][] Pattern = new int[2][GroupedCharList.size()];
        {
            int Counter = 0;
            for (char C : GroupedCharList)
            {
                Pattern[0][Counter] = Ids[C - 'a'];
                Pattern[1][Counter] = GroupedFreqList.get(Counter);
                Counter++;
            }
        }
        return Pattern;
    }

}
