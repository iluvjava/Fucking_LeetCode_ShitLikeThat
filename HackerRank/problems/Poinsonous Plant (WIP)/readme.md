# Problem Statement

* If a plant has more pesticide than the plant on its left, then it dies. 

* After how many days, that plants are gonna stop dying... ?

* Facts:
  * If the sequence is **monotonically decreasing**, then the plants won't really die. 
  * If the sequence is **monotonically increasing**, then the plants die all at one day. 

### Idead 1: Brute Force Simulation
* This is going to be very slow. 

### Do it by hands. 

* What if:
  * for each element in the array, find the first element on its left that is larger than that given element? 
  arr: `6 5 8 4 7 10 9`
  idx: `0 1 2 3 4 5  6`
  * 0 ---> -1
  * 1 ---> 0
  * 1 
  * Expected answer: 2 days. 

* What if we have 2 sequence of monotonically decreasing sequences concated together? 
  * 4, 3, 2, 1, 4, 3, 2, 1
  * 4, 3, 2, 1, 3, 2, 1
  * 4, 3, 2, 1, 2, 1
  * 4, 3, 2, 1, 1
  * Won't change anymore. 
  * Notice that, for each element, if we look for the number to the right that are immediately smaller/equal, then 
  the maximum distance is the number of days which, the plant eventually stop dying. 
  * Observer how that plant with poisonous level of 1 is killing all the plants that comes after it.

* we look through the array in reverse, and then we try to maintain a **monotonically increasing sequence** 
from bottom to the top in our stack (Or vice versa like mono decreasing from top to bottom and travese in the 
natural order of the element in the queue) 
structure. 
  * Top [4, 3, 2, 1] Bottom
  * Top [1] Bottom  # The 1 plants killed all the plants that has less poisons coming after it, in 4 days. 
  * (...)
  * Top [4, 3, 2, 1, 1] Bottom

### This is what I think about the solution: 
* Example: `6 5 8 4 7 10 9`
  * Top [10, 9] Bottom  # add 7
  * Top [7] Bottom.  # 7 killed the 2, that is 2 days. 
  * Top [4] Bottom.  # 4 killed 7, in 2 days. 
  * Top [8, 4] Bottom 
  * Top [5, 8] Bottom  # 5 killed 8, in 1 day. 
  * Top [6] Bottom  # 6 killed 8, in 1 day. 
* The maximum days needed to kill all of them should be 2.

* Do there exist a counter example that break our shit? 
  * Monotone decreasing: works 
  * Monotone increasing: works
  * Single ton: works

* I am just gonna code it out and see how well it works for the problem 