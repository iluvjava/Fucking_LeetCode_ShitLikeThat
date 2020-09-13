## Problem Statement

* String A is the child of String B if there eixsts a set of letter to remove in string B such that, after the 
editing, String B will become string A.

* Input: 2 strings, s1, s2

* Output: The longst child of both string. 
  * This is the same thing as asking for the Longest Common Substring. 

## Algorithm

* We need the classic bottom up approach to the longest common substring problem, and then improve the memorhy aspect
by only using on array to store the itermediate results. This is the only way to solve it. 

* The solution in python didn't past the test because python is just too slow, but the implementations in java passes
the test easily. 

