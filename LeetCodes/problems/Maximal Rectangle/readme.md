# Maximal Rectangle

* [link](https://leetcode.com/problems/maximal-rectangle/)

* Given a 2d arrays with only 1, 0s, is find the size of the maximal rectangle containing only
1s.

* Standing Assumptions:
  * Indexing from 0.
  * The top left corner of the array is the [0, 0]

## Idea 1

* Recurrences, let's define that, T[I, J] gives the maximum continous block of 1 square such that its bottom
left corner is located at the index [I, J].

* No recrusive formulation is discovered.

## Idea 2 (Thinking about 1D, Rows and Columns)

* [0, 0, 1, 1, 0, 1, 1, 1]
  * T[I] := 1 + T[I - 1] if `I` th place is a 1.
  * Else, it breaks, and it's gonna be 0.

* So for each row, we can compute the longest continous bar, and for each column, we can do that too.

* How does it helps with the 2D?

* We need multiple Tables to store them
  * T1, T2 for rows and columns, T3 for The maximum rectangle that located at the bottom right of the sub [I, J] matrix.
  T1, T2 are 1d with length equal to the the number of rows and columns.
  * Then, we need to update them:
    * RowConitnousSubBar = T1[I - 1, J]
    * ColCotinousSubBar = T2[J - 1]
    * MaxRectR, MaxRectC = T[I - 1, J - 1]
  * If the current cell is a 1, then we are good to improve the maximum for the rows and columns and the rectangle.
    * T1[I] = T1[I - 1] + 1
    * T2[J] = T2[J - 1] + 1
    * T[I, J] = (min(MaxRectR, RowContinousSubBar) + 1, min(MaxRecC, ColContinousSubBar + 1))
  * Else, it's not 1, then it breaks the row, the column, and the rectangle. 
  

* Base case, ZEROES, there are no square, no things, outside of the 2d array.

