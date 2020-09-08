# Problem Statement: 

* Given a string with characters in it, determine the minimum number of characters deletions from the string
such that, all the adjacent characters in the string will be different from each other. 

* Solution
  * use a stack, the current character is different from the one on the top of the stack, then just 
  add that number of deletions. 