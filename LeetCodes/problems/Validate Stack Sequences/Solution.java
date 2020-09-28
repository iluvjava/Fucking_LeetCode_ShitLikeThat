import java.util.Stack;

class Solution
{

    public static void main(String[] args)
    {
        int[] Pushed = new int[]{1, 2, 3, 4, 5};
        int[] Popped = new int[]{4, 5, 3, 2, 1}; 
        System.out.println(validateStackOperations(Pushed, Popped));
        Pushed = new int[]{1, 2, 3, 4, 5};
        Popped = new int[]{3, 2, 1, 4, 5};
        System.out.println(validateStackOperations(Pushed, Popped));

    }

    public static boolean validateStackOperations(int[] pushed, int[] popped)
    {
        // Queue<Integer> Popped = new LinkedList<>();
        int J = 0;
        Stack<Integer> TheStack = new Stack<>();
        for (int I : pushed)
        {
            TheStack.push(I);
            while (J < popped.length && !TheStack.isEmpty() && TheStack.peek() == popped[J])
            {
                TheStack.pop();
                J++;
            }
        }
        
        return J == popped.length;
    }

}