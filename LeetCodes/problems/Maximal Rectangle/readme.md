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
  * T1[I, J]:
    * The longest continous bars of 1 on the row, the indexer [I, J] means that bar's right end located at [I, J], the
    it column and the J th row, and the T1[I, J] is the length of that continous bar.
  * T2[I, J]:
    * It's the same as the row bar.
  * T[I, J]:
    * It's a value of a tuple, say (H, W), and it H is the height of the largest continous rectangle such that its
    right bottom corner locats at (H, W) in the array, and W is the width.
  * Then, we need to update them in a forloop:
    * RowConitnousSubBar = T1[I - 1, J]
    * ColCotinousSubBar = T2[J - 1]
    * MaxRectR, MaxRectC = T[I - 1, J - 1]
  * If the current cell is a 1, then we are good to improve the maximum for the rows and columns and the rectangle.
    * T1[I, J] = T1[I - 1, J] + 1
    * T2[I, J] = T2[I, J - 1] + 1
    * T3[I, J] = (min(MaxRectR, RowContinousSubBar) + 1, min(MaxRecC, ColContinousSubBar) + 1)
  * Else, it's not 1, then it breaks the row, the column, and the rectangle.
    * Set all of them to be zero. after that point.

* Keep a running sum maximal that is the area of the square while forlooping through the 2d array.

* Base case, ZEROES, there are no square, no things, outside of the 2d array.

## Random Idea 2.1

* If we used multiple table, then is the recursive formulation of the algorithm gonna be multi-recursive? Like
recursion but with multiple functions?

## What failed 
* For some reasons I just cannot get it right and the solution exploded as I add more and more 
handling for the edges cases, I might be "overfitting" so I googled the correct solution instead. 

## Idea 3 

* The solution for the problem can be found here: (link)[https://www.geeksforgeeks.org/largest-rectangle-under-histogram/]

### Largest Rect In Histogram Sub Routine

* Construct the longest continuous 1 array for each horizontal level on the matrix. 

* For each level, find the largest rectangle on the histograms. 

#### Algorithm

* Hist: A array of positive integer, representing all the bars of on the axis. 

* Stack: The indices of all the bars, such that, the bars will be increasing order of their heights.

* Monotonic Hitogram
```
*
* *
* * *
* * * *
```

* The sets of rectangles that can have maximum sizes are
```
*  
*   * *
*   * *  * * *
* , * *, * * *, * * * *
```
* if not, extending it to the left side will improve the size. 

* Now we exploit this property for our algorithm. 

* Assuming a stack of bars are given, with their height, and from the top of the stack to the bottom
they are in decreasing height. 

* 
