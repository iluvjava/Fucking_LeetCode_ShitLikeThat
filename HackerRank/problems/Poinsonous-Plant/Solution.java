import java.util.*;
import java.lang.System;

class Solution {

    public static void main(String[] args)
    {
        { // This is the first test. -----------------------------------------------------------------------------------
            System.out.println("Has been running");
            int arr[] = new int[]{1, 2, 3, 4, 2, 3, 4};
            System.out.println("Output:");
            LinkedList<LinkedList<Integer>> Groups = GroupsIt(arr);
            System.out.println(Groups);
            solution_cancellation(Groups);
            System.out.println(Groups);
        }

        {
            System.out.println();
            int arr[] = new int[]{3, 5, 8, 6, 4};
            LinkedList<LinkedList<Integer>> Groups = GroupsIt(arr);
            System.out.println("Initial Groups: \n" + Groups);
            solution_cancellation(Groups); 
            System.out.println("After Cancellation:\n" + Groups);
            System.out.println("Expect it to be 3");
            System.out.println(solution(arr));
        }


        {  // Test the whole thing out
            int arr[] = new int[]{1, 5, 4, 3, 2};
            System.out.println("Expect it to be 4");
            System.out.print(solution(arr));
        }

    }

    public static int solution(int[] arr)
    {
        LinkedList<LinkedList<Integer>> Groups = GroupsIt(arr);
        int Counter = 0;
        while (Groups.size() >= 2)
        {
            Counter++;
            solution_cancellation(Groups);
            solution_merge(Groups);
        }
        return Counter; 
    }

    public static LinkedList<LinkedList<Integer>> GroupsIt(int[] arr)
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
        return Groups;
    }

    public static boolean solution_cancellation(LinkedList<LinkedList<Integer>> arrs)
    {
        ListIterator<LinkedList<Integer>> Litr = arrs.listIterator(0);
        {
            LinkedList<Integer> Pre = Litr.next();  // Skip the first list. 
            while(Litr.hasNext())
            {
                LinkedList<Integer> Cur = Litr.next();
                Cur.removeFirst();
                if (Cur.size() == 0)
                {
                    Litr.remove();
                }
            }
        }
        return true;
    }

    public static boolean solution_merge(LinkedList<LinkedList<Integer>> arrs)
    {
        Iterator<LinkedList<Integer>> Itr = arrs.iterator();
        LinkedList<Integer> Pre = Itr.next();  // Take out the first 
        {
            while (Itr.hasNext())
            {
                LinkedList<Integer> Cur= Itr.next();
                if (Cur.getFirst() <= Pre.getLast())
                {
                    Pre.addAll(Cur);  // Concat that thing.
                    Itr.remove();
                }
                else
                {
                    Pre = Cur;
                }
            }
        }
        return true;
    }

    
}