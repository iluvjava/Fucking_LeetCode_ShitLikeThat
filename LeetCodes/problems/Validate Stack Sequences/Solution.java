import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

class Solution
{

    public static void main(String[] args)
    {
        int[] Pushed = new int[]{1, 2, 3, 4, 5};
        int[] Popped = new int[]{4, 5, 3, 2, 1}; 
        validateStackOperations(Pushed, Popped);
    }


    public static boolean validateStackOperations(int[] pushed, int[] popped)
    {
        Queue<Integer> Pushed = new LinkedList<>();
        Queue<Integer> Popped = new LinkedList<>();
        Stack<Integer> TheStack = new Stack<>();
        while (!Pushed.isEmpty())
        {
            Pushed.add(Pushed.poll());
            while (!TheStack.isEmpty() && TheStack.peek() == Popped.peek())
            {
                TheStack.pop();
                Popped.poll();
            }
        }
        return Pushed.size() + Popped.size() == 0;
    }

}