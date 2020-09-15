
* Input Example: 

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


## 2 Stacks Evaluate with Brackets.

* (`2*3 - (5 + 6*7)) - 8`
  * [2, 3], [*], [(]; - doesn't precede *
  * [6], [-], [((];
  * [6, 5], ,[-], [((]

  
* https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/


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
  * if ( +1, ) -1 