# Problem Statement

* (Link)[https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms]

* L[i]:
  * How important the contest is.

* T[i]:
  * How much luck points is lost/obtained for this contest.

* K:
  * The maximum number of important contest that, Lena is allowed to lose.

* Lena is interested in getting the maximal luck she can have after the contest.

## The ideas

* There are 2 type of contest we can lose, and one of them is limited by a certain number.

* We seperate the groups into 2, the important and the unimportant one.
  * The number of important loses is less thank K.
    * Among all the important loses, we need to maximizes the lost point by sorting all the important contests. 
    Descending order of luck points. 
    * So that, we maximizes the luck point we saved for the contest.
  * The number of unimportant loses can be as much as we want.

