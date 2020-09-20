import java.util.Arrays;

class Solution {

    public static void main(String[] args)
    {
        

    }

    public static int solution(int[] prices, int k)
    {
        Arrays.sort(prices);
        int ToysCount = 0;
        for (int I = 0; I < prices.length && k >= 0; I++)
        {
            k -= prices[I];
            if (k >= 0)ToysCount++;
        }
        return ToysCount;
    }
}