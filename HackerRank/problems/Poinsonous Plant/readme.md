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

* The solution passed a majority of tests, but there are few tests that we got the wrong answers for.

* Failed Minimum Inputs: [3, 5, 8, 6, 4]
  * Top [3] Bottom
  * Top [3, 5] Bottom  # Day ++
  * Top [3, 5, 8] Bottom  # Day ==
  * Top [3, 5, 8, 6] Bottom  # Day ==
  * Top [3, 5, 8, 6, 4] Bottom  # Day ==

## A special Case where the first element is the global minimum of the array

* let's see, we know that, 3 is the global minimum, hence it has to kill all the other plants at some point, and
let's only investigate the case where, the start of the array is the global minimum of the array.

* 3, 5, 8, 6, 4
  * Incrase, Increase, decrease, decrease.
  * Each time it decrases, we add 1, for the whole chunk of increasing, we don't add anything.
    * We this because, 3 is the global minimum.
* 3, 4, 6, 9, 7, 5
  * `(Increase, Incrase, Incrase): + 1, (decrase, decrease): + 2 = (result): 3`
  * 3 days for all of them to die.
* 3, 8, 5, 6, 4
  * (Incrase: +1) + (decrase*3: + 3) = (results: 4)

* 1, 2, 2, 3, 3, 4
  * 1, 2, 3
  * 1
  * 2 steps in total.
  * ([1, 2, 2, 3, 3]: Incrase --> + 1) + ([3, 4]: decrase --> + 1)
  * Yep... matched.

* Let's have a hard one.
* 1, 2, 3, 4, 3, 4, 5, 6, 2, 3, 4, 5
* 1, 3, 2  # Day 1
* 1, 2  # Day 2
* 1  # Day 3
* ([1, 2, 3, 4]: Increase --> + 1) +
* ([4, 3]: Decrase --> + 1) +
* ([3, 4, 5, 6]: Increase --> + 1) +
* ([6, 2]: Decrease --> + 1) +
* ([2, 3, 4, 5]: Increase --> + 1)

* We failed. (sad face)

## The correct Solution: (Simultaneous decay of multiple-monotone subsequences in stacks)

* Using multiple stack, where each stack is a monotone decreasing subsequence, they server as the playground for
use to simulate the plant dying. The clever part of the solution is the use of the data-structure which can give
it an incredible run time.
* Data structure to leverage: LinkedList<LinkedList<Integer>>, probably gonna need java.
* Input: [1, 2, 3, 4, 5]
  * Parse into parallel stacks:
  * [[1], [2], [3], [4], [5]] # First day.
  * [[1][0] < [2][0] < [3][0] < [4][0] < [5][0]]
  * [[1]] # after day 1, terminate and that is all we need.

* Input: [3, 5, 8, 6, 4]
  * [[3][0] < [5][0] < [8, 6, 4][0]]
  * [[3][0] < [6, 4][0]]  # after day 1
  * [[3][0] < [4][0]]  # after day 2
  * [[3]]  # after day 3

* Input: [1, 2, 3, 4, 3, 4, 5, 2, 3, 4]
  * [[1], [2], [3], [4, 3], [4], [5, 2], [3], [4]]
  * [[1],           [3],         [2]             ]  # after cancellation
  * [[1], [3, 2]]  # after merge
  * [[1], [2]]  # after cancellation
  * [[1]]  # after cancellation
  * 3 round cancellation --> 3 days.

* Summary:

* (1) Construct a list of monotone decreasing sequences from the array, such that the first.
  element of each linkedlist is larger than the last element in the previous linkedlist. Name that lists of lists 
  to be `Groups`.

while(There are more than one list in the `Groups`):
  run: Cancellation Subroutine.
  run: Merge Subroutine.
  Increment: The number of days.

Output: The numeber of days is the result we want. 