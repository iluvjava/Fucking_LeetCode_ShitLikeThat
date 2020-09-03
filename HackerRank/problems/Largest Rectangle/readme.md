# Problem Statement

* Given a bar chart, represented by integers, find the area of the largest rectanlge in that bart chart.

* This problem is classic and it's the sub routine used in the detection of the largest rectangle
in a 2d array.

* Exploiting the monotoniticity of the sequence.

## Algorithm (This is wrong)

* The algorithm involved in this problem uses the monoticity.

* Let's define a stack invariant:
  * From the bottom to the top of the stack, the elements are in ascending order.

```python
      *
    * *
  * * *
* * * *
```

* Then the area for all the rects hidden in the graph is gonna be like:
  * 4, 6, 6, 4

* Psuedo Codes:

## Algorithm (From Stackoverflow)

* I found the solution for the problem on the stackover flow, and this is a very clever one that use the same idea
as the one they get in Geek for Geek.

```python
def largestRectangleArea(A):
    ans = 0
    A = [-1] + A
    A.append(-1)
    n = len(A)
    stack = [0]  # store index
    for i in range(n):
        while A[i] < A[stack[-1]]:
            h = A[stack.pop()]
            area = h*(i-stack[-1]-1)
            ans = max(ans, area)
        stack.append(i)
    return ans
```

* Algorithm (Divide and Conquer)

* Sub problem is solved.

* When merging, we are only worrying about the rectangles that include the right-most bars from left, and left-most
bar from right.

## Other Idea (A divide by conquer approach)

* This idea might not be applicable here because the problem is under the "Queue and Stack section"

## Moral of the story

* Stack can help with extracting information about the: Nearest element that is larger/smaller than the current 
element.
