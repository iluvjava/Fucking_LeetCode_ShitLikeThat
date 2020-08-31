# Problem statement. 

* Ammong all the possible continous sub-array in the array, find the value of the maximal sum. 


## Solution

* This problem can be solved in so many ways, normally people will go with the slicding window approach, but here
I an thinking of a dynamic programming approach to the problem.

* Recurrence:
  * T[I] = max(T[I - 1] + arr[I], arr[I])
    * there are 2 cases here. Either the current element is part of the solution, or it's not. 
    * If it's not, then it will not be contributing to the sum. 
    * If it is, then it will be added up to the sum. 
    * Keep the maximum of it, and we should have the solution. 