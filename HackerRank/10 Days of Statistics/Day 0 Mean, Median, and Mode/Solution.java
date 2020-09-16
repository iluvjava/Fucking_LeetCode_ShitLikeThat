import java.util.*;
import java.lang.System;
class Solution
{
    public static void main(String[] args)
    {
        int[] data = readFromStdIn();
        MMMAnalyzer ana = new MMMAnalyzer(data);
        System.out.println(ana.average);
        System.out.println(ana.median);
        System.out.println(ana.mode);
    }

    public static int[] readFromStdIn()
    {
        Scanner sc = new Scanner(System.in);
        sc.nextLine();
        String[] Ints = sc.nextLine().split(" ");
        int[] data = new int[Ints.length];
        for (int I = 0; I < Ints.length; I++)
        {
            data[I] = Integer.parseInt(Ints[I]);
        }
        return data;
    }
}

/**
 * It analyze the inputs data. 
 * 
 */
class MMMAnalyzer
{
    public double median;
    public double average;
    public int mode;  // as small as possible if frequencies are the same. 
    public int[] data; 

    public MMMAnalyzer(int[] arr)
    {
        Arrays.sort(arr); // Important. 
        data = arr;
        getMedian();
        getAverage();
        getMode();
    }

    public void getMedian()
    {
        int M1 = data.length/2;
        int M2 = data.length%2 == 0? M1 - 1: M1;
        median = (data[M1] + data[M2] + 0.0)/2;
    }

    public void getAverage()
    {
        long Accumulate = 0;
        for(int I = 0; I < data.length; I++)
        {
            Accumulate += data[I];
        }
        average = (Accumulate + 0.0)/data.length;
    }

    public void getMode()
    {
        int NumberWithMaxFreq = data[data.length - 1];
        {
            int MaxFreq = 1;
            int RunningFreq = 1;
            for (int I = data.length - 1; I >= 1; I--)
            {
                if(data[I] == data[I - 1])
                {
                    RunningFreq += 1;
                }
                else
                {
                    RunningFreq = 1;
                }
                if (RunningFreq >= MaxFreq)
                {
                    NumberWithMaxFreq = data[I - 1];
                    MaxFreq = RunningFreq;
                }
            }
        }
        mode = NumberWithMaxFreq;
    }

}