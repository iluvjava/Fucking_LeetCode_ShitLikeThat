
/**
 * neighbours both active or both inactive, the cell becomes inactive the next day. 
 * for cells that are beyond the left end and right end, assume them to be always inactive.
 */
import java.lang.System;
import java.util.Arrays;
class AmazonDemoStratchpaper {

    public static void main(String[] args)
    {
       int[] After = cellCompete(new int[]{1, 0, 0, 0, 0, 1, 0, 0}, 1);
       System.out.println(Arrays.toString(After));

       System.out.println(GCD(2, 3));

       System.out.println(generalizedGCD(new int[] {5, 10, 25, 40, 60}));
    }

  //METHOD SIGNATURE BEGINS, THIS METHOD IS REQUIRED
  /**
   * Operation is muttable 
   */
  public static int[] cellCompete(int[] cells, int days)
  {
    int[] CellsAugmented = new int[cells.length + 2];
    while(days-- > 0)
    { // Simulate
        
        for (int I = 0; I < cells.length; I++) 
        CellsAugmented[I + 1] = cells[I];
        
        for (int I = 0; I < cells.length; I++)
        {
            if (CellsAugmented[I] == CellsAugmented[I + 2])
            {
                cells[I] = 0;
            }
            else
            {
                cells[I] = 1;
            }
        }
    }
    return cells;
  }

  /**
   * Find the Greatest common divisor among all the numbers in the array. 
   *   Divide and conquer approach. 
   * @param arr
   * @return
   */
  public static int generalizedGCD(int arr[])
  {
    return generalizedGCD(arr, 0, arr.length);
  }

  /**
   * Start inclusive, end not inclusive. 
   * @param arr
   * @param start
   * @param end
   * @return
   */
  public static int generalizedGCD(int arr[], int start, int end)
  {
    if (end - start <= 2)
    {
        if (end - start == 1)
        {
            return arr[start];
        }

        return GCD(arr[start], arr[end - 1]);
    }
    int M = (end + start)/2;
    int D1 = generalizedGCD(arr, start, M);
    int D2 = generalizedGCD(arr, M, end);
    return Math.min(D1, D2);
  }

  /**
   * Method comes from memory from cs classes. 
   * @param a
   * @param b
   * @return
   */
  public static int GCD(int a, int b)
  { 
    if (b == 0) return a;
    if (a < b) return GCD(b, a);
    return GCD(b, a%b);
  }




}