# Problem Statement

* Given a bar chart, represented by integers, find the area of the largest rectanlge in that bart chart.

* This problem is classic and it's the sub routine used in the detection of the largest rectangle
in a 2d array.

* Exploiting the monotoniticity of the sequence.


## Algorithm

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

```python
Hist  # The heights of all the bars in the histogram
Stack  = []  # The index of the bars in the hist
RunningMax = 0  # Maximum area of the hidden rectangle
for I in range(len(Stack)):
    if len(Stack) == 0 or (Hist[I] >= Stack[-1]):
        Stack.append(I)
    else:
        Counter = 1
        while len(Stack) != 0:
            Bar = Hist[Stack.pop()]
            RunningMax = max(RunningMax, Bar*Counter)
            Counter += 1
        Stack.append(I)
```