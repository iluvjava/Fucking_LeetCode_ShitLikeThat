## Hackerrank Left Rotation

* [link](https://hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays)

* Problem description is a PDF under the current directory. 

### Approach

* simply just make a new array and them copy the element with an offset, and then go back and copy the remaining parts. 

* A better approach is to only allow for swapping 2 element to reach the desired configuration. For example if we were 
to rotate the to the left by 1, array with size 6, then it looks like this:

* Note: this is my failed approach, I fought valiantly with it but failed. 

```python
[0, 1, 2, 3, 4, 5]; Initial
[1, 0, 2, 3, 4, 5]; swap(0, 1)
[1, 2, 0, 3, 4, 5]; swap(1, 2)
(...)
```

* We applied a "filter" with width of 1, and sweep it through from left to right.

* Now let's rotate it by 2

```python
[0, 1, 2, 3, 4, 5]; Initial
[2, 1, 0, 3, 4, 5]; (0, 2)
[2, 3, 0, 1, 4, 5]; (1, 3)
[2, 3, 4, 1, 0, 5]; (2, 4)
[2, 3, 4, 5, 0, 1]; (3, 5)
```

* Now let's see if it works for 3

```python
[0, 1, 2, 3, 4, 5]; Initial
[3, 1, 2, 0, 4, 5]; (0, 3)
[3, 4, 2, 0, 1, 5]; (1, 4)
[3, 4, 5, 0, 1, 2]; (2, 5)
```

* Consider a rotation of **4**, which is a right rotation in the other direction, by **2**.

```python
[0, 1, 2, 3, 4, 5]; Initial
[0, 1, 2, 5, 4, 3]; (3, 5)
[0, 1, 4, 5, 2, 3]; (2, 4)
[0, 5, 4, 1, 2, 3]; (1, 3)
[4, 5, 0, 1, 2, 3]; (0, 2)
```

* Array len: 8, rotation 3

```python
[0, 1, 2, 3, 4, 5, 6, 7]; Initial
[3, 1, 2, 0, 4, 5, 6, 7]; (0, 3)
[3, 1, 2, 0, 4, 5, 6, 7]; (1, 2)
```

* Yes, of the rotation is less than half, swap from left to right, else, swap sequentially from right
to left.

  * What if the size of the array is odd? The example is even...

* Consider a rotation of 3, just over half.

```python
# From left to right: 3
[0, 1, 2, 3, 4]; Initial
[3, 1, 2, 0, 4]; (0, 3)
[3, 4, 2, 0, 1]; (1, 4)
# from right to left: 3?
[0, 1, 2, 3, 4]; Initial
[0, 4, 2, 3, 1]; (1, 4)
[3, 4, 2, 0, 1]; (0, 3)
```

* We failed it doesn't work.

### The Algorithm

* Precondition: The array have even length

* Make 2 running index with a distance of of d.
  * Run it from left to right if d <= n//2, n: size of the array.
  * Run it from right to left if d >= n//2, n: size of the array.
    * change the distance between 2 running index from d to n - d
* Terminates when one of the running indices reaches the end of the array.

### The big brain solution: A Juggling Algorithm

* [Link](https://www.geeksforgeeks.org/array-rotation/)

### Small Brain solution

* Just make an auxilary array and then copy the element over with an offet.
