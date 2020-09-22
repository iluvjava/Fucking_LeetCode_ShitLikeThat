# Problem Statement

* Give a 2d array such that:
  * The integers in the rows are sorted in ascending order from left to right.
  * The integers in the columns are sorted in ascending order from top to bottom.

* Then we know the following.
  * arr[I, J] <= arr[I + 1, J], arr[I, J + 1]
  * Then, iterating throug the matrix, diagonally, from the top left corner to the bottom right corner, while going
  down will produce a sequence of intergers that are in ascending order.

# Idea 1 Use a Hammer

* Brute Force:
  * O(MN), just seach each entry for the element and see if it's there or not.

# Idea 2 Coordinate Descend to reduce the search space

* Row/Col moves the pointer on the matrix to look for the number. 
  * This idea is directly borrowed from the idea of coordinate descend. 
  
* Complexity O(M + N)

# Idea 3 Bijective Mapping of Matrix Entry

* Design a one to one function that convert the `1 <= I <= M*N`, and it must be the case that, as I increases, the
entry get from the matrix is also increasing
  * Use the diagonal strategy that got mentioned before.

* Then use this function to wrap around the matrix and then use the binary search algorithm to look for the number in
the matrix.

# Idea 3 A Divide and Conquer Approach

* This is a possible exploit by spliting the matrix into 4 sub parts, and it will be deteremined that, the 
top left corner of the matrix is always less than the bottom right corner matrix. 
