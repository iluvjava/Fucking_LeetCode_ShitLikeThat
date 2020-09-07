import java.util.*;
class Solution
{
    public static void main(String[] args)
    {
        int[] data = new int[]{1, 3, 3, 5, 8 ,7, 7, 9, 0};
        
    }
}

/**
 * It analyze the inputs data. 
 * 
 */
class MMMAnalyzer
{
    protected int median;
    protected double average;
    protected int mode;  // as small as possible if frequencies are the same. 
    protected int[] data; 

    public MMMAnalyzer(int[] arr)
    {
        Arrays.sort(data); // Important. 
        getMedian();
        getAverage();
        getMode();
    }

    public void getMedian()
    {
        int M1 = data.length/2 + 1;
        int M2 = data.length%2 == 1? M1 + 1: M1;
        median = (data[M1] + data[M2])/2;
    }

    public void getAverage()
    {
        long Accumulate = 0;
        for(int I = 0; I < data.length; I++)
        {
            Accumulate += data[I];
        }
        average = Accumulate/data.length;
    }

    public void getMode()
    {
        int NumberWithMaxFreq = data[data.length - 1];
        {
            int MaxFreq = 1;
            int RunningFreq = 0;
            for (int I = data.length - 2; I >= 0; I--)
            {
                if(data[I] == data[I - 1])
                {
                    RunningFreq += 1;
                    if (RunningFreq >= MaxFreq)
                    {
                        NumberWithMaxFreq = data[I];
                        MaxFreq = RunningFreq;
                    }
                }
                else
                {
                    RunningFreq = 1;
                }
            }
        }
        mode = NumberWithMaxFreq;
    }

}