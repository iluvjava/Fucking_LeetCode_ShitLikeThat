# Problem Statement

* Given an infix expression with operators: `+, -, *, /, (, )`, evaluate the expression involving operands that are
only positive integers.

## Alto's Approach

* Input Example

* (1 + 1)*(2 + (3 - 7)/6)

* Base Case:
  * 1 + 1, (2 + ???/???)

* Infix to post fix, simple expressions:
* "(1 + 1 * 5)" ===> "1, 1, +, 5 *"
  * Doueble Stack:
    * [1, 1], [+], "*5"
    * [1, 1], [+], * precedes +; just add in
    * [1, 1, 5], [*, +]
  * PostFix: 1, 1, 5, *, +

* "2*3+4-5"
  * [2, 3], [*]; + doesn't precede *
  * [6, 4], [+]; - doesn't matter
  * [6, 4, 5], [-, +]; end.
  * Evalueate 2 stacks:
    * [6, -1], [+]
    * [5], []

## 2 Stacks Evaluate with Brackets

* (`2*3 - (5 + 6*7)) - 8`
  * [2, 3], [*], [(]; - doesn't precede *
  * [6], [-], [((];
  * [6, 5], ,[-], [((]

* https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/

* Algorithm, consider a set of operators and operands, where all the operators are binary, and the expression is
valid.
  * Components
    * Stack1: The Operands: Numbers, and parenthesis.
    * Stack2: The operators: Binary operators with different precedence.
    * Queue1: The queue that stores all the operators and operands in infix ordering.
    * Queue2: PostFixQueue: A queue to store the post fix expression.
    ```
    while (Queue1 is not empty):
      E = Queue1.dequeue()
      if (E is a number):
        Stack1.append(E)
      else if (E is Closing parenthsis):
        Flush: Stack1, Stack2 to Queue2 util opening parenthsis are met.
        pass
      else: // E is operators, or opening parenthsis
        if (operator on top of the stack has an higher precedence):
          Flush: Stack1, Stack2 to Queue2 util current operator has the same or higher prededence than the operator 
          on the top of the Stack2
    Flush: All remaining stuff in Stack1, Stack2
    ```

    * Queue2: Now it contains the postfix expression in the correct order.

  * 3+(5-6)*2

  ```
    Stack1 = []; Stack2 = []; Queue1 = [3, +, (, 5, -, 6, ), *, 2], Queue2 = []
    [3, (, 5, 6]; [+, -]; [), *, 2]; []
    [3]; [+]; [*, 2]; [6, 5, -]
    [3, 2]; [+, *]; []; [6, 5, -]
    []; []; []; [6, 5, -, 2, *, 3, +]
  ```

  * Evaluate Postfix Expression (This is the final part of the story)
  

#### Yuxuan

* Base Case: "  3", "4", " 5  "
* if exists brackets:
  * calculate(s.beforeBracket + calculate(s.inBracket) + s.afterBracket)
* else if exists * or /:
  * calculate(s.before*/ + calculate(_ * _) + s.after*/)
* else if exists +/-:
  * calculate(...)
* else
  * return parseInt(s)

* 3*(2 - 0)
  * if ( +1, ), - 1