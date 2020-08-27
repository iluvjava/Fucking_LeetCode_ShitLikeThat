# From Problem Statement

* Min: Total amount of candies.

* Constraint: If 2 children sit next to each other, then the one with higher score get more candies.

* Constraint: All student must get at least one candy.

* Problem didn't say what happen if the student next to each other happen to have the same score. So I will assume in that case, just go for the 
absolute minimum for that student, that is, 1 candy.

## Idea 1 (Recursive formulation for the problem)

* Because the this is a minimization problem, and it's ultimately feasible, hence we need too look for an
lowerbound on candy for each of the children.

* take [4, 6, 4, 5] for example.

* Define T[I] to be the minimum amount of candies needed for the I th student in the row, denote `n = len(arr)`
  * for all `1 <= I < n - 1`
    * if arr[I] > arr[I - 1] then T[I] >= T[I - 1] + 1 
    * if arr[I] > arr[I + 1] then T[I] >= T[I + 1] + 1
    * arr[I] >= must be asserted. 
  * For I = 0, I = n - 1, modify the above relation, it's a special case of that. 


## Idea 1.1 (Mem + Recur)

* Use an array/dictionary to store the minimum canides for the recursion. 

* Problem: StackOverflow. 

## Idea 1.2 (Stackification)

* Don't... Pop it... until the solution has been merged in. 


