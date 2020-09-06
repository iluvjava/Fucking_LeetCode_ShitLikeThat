import java.util.*;
import java.lang.System;

class Solution {

    
    public static void main(String[] args)
    {
        System.out.println("Has been running");
        int arr[] = new int[]{1, 2, 3, 4, 2, 3, 4};
        System.out.println("Output:");
        LinkedList<LinkedList<Integer>> Groups = GroupsIt(arr);
        System.out.println(Groups);
        solution_cancellation(Groups);
        System.out.println(Groups);

    }

    public static int solution(int[] arr)
    {
        LinkedList<LinkedList<Integer>> Groups = GroupsIt(arr);
        int Counter = 0;
        while (Groups.size() >= 0)
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
            }
        }
        return true;
    }

    
}