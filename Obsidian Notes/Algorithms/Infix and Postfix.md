## Conversion and Evaluation

### The Shunting Yard Algorithm (Expression Tree)

* This is not directly related to graph, but the thing that is operating under it, it's a tree, a special type of
graph.

* The Expression tree represent an mathematical expression involving operators and operands.
  * Human can read an expression that is written as an infix expression, and the infix expression is the same
  as traversing the expression tree with Inorder Traversal.
  * The bracket in the expression represents some syntactical meaning, and it represents the whole sub tree
  in the expressioen tree.
  * Important Components
    * Operands stack, Operator stack, Output Queue, Input Queue.

    ```
      OptStack = []; OutputQueue = []
      foreach(Token in the infix expression):
          if (Token is operand):
            Append it to the output list.
          if (Token is left parenthesis):
            push it to the OptStack
          if (Token is right parenthsis):
            Flush all the operators that comes after the left parenthesis in the stack.
          if (Token is an operator):
            if (Token on top of OptStack is higher than the current operator):
              Flush all operators to the output queue until one with equal rank is met.
            else:
              Just put it to the OptStack.
    ```

  * Leetcode Simple calculator asked about it.

