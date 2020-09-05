import java.util.*;

class Solution {

    public static void main(String[] args)
    {
        
    }

    public static int solution(int[] arr)
    {
        LinkedList<LinkedList<Integer>> Groups = new LinkedList<>();
        {
        // Construct list of monotone decreasing sub sequenes. ---------------------------------------------------------
            LinkedList<Integer> TheFirst = new LinkedList<>();
            TheFirst.add(arr[0]);
            Groups.add(TheFirst);
            for(int I = 1; I < arr.length; I++)
            {
                Integer LastofLast = Groups.getLast().getLast();
                if (arr[I] > LastofLast)
                {
                    LinkedList<Integer> NewOne = new LinkedList<Integer>();
                    NewOne.add(arr[I]);
                    Groups.add(NewOne);
                }
                else
                {
                    Groups.getLast().add(arr[I]);
                }
            }
        }
        while (Groups.size() >= 0)
        {

        }
        return 0; 
    }

    public static boolean solution_cancellation(LinkedList<LinkedList<Integer>> arrs)
    {
        ListIterator<LinkedList<Integer>> Litr = arrs.listIterator(1);
        while(Litr.hasNext())
        {
            
        }
        return true;
    }

    public static boolean solution_merge(LinkedList<LinkedList<Integer>> arrs)
    {
        
        return true;
    }
}