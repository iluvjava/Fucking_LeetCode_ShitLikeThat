# Hidden Bonus Problem

* This problem is a hidden problem used for the skill(intermediate) certificate on Hackerrank.

* Given an array of integers, we want to pair up numbers such that each pair has a absolute difference that is larger

than a given threshold, we want to find the number, representing the maximum number of pairs we can make out of the

data set.

* Please also consider the case where the array of numbers are sorted.

* Special case:

* Inputs: mindiff = 1, arr = [1, 1, 1, 1, 2], only one pair can be made.

* mindiff = ~, arr = [1, 1, 1, 1, 2, 2, 10], 2 can only pair with 1, but 10 can pair with all others.
  * If 10 is chosen to pair of with 2, then one of the 2 is wasted because 10 also have the choice to pair of 1.

  * So for each 1, we want to pair with the closest on on the right side such that it's immediately larger than mindiff.
  * For all other numbers that are right to the 1, their pairmate should be further down in the array. 

* Assuming that, the minimum pairing strategy works correctly (Pairing pair that are immediately larger on the right 
side)


