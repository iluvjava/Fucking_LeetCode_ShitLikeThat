# Problem Statment

* Given array of integers have an visual representation of block:
    ```
      *   *     *   *
      *   * *   *   *
      *   * *   *   *
      *   * * * * * *
    * *   * * * * * *
    * *   * * * * * *
    ```

* Determine the amount of rain water can be trapped here.

# Idea1

* Use a stack. Monotonically Decreasing and flushes when to keep the monotonicticity
  * When doing the fushing, this is the perfect chance for computing the quantity we need.

* Let's take a look a at basic valley:

  ```
  *           *
  * * *   *   *
  * * * * *   *
  ```

  * Array rerpesentation: [3, 2, 2, 1, 2, 0, 3]

* We will focus on the flushing mechanics, def `Total := 0`
  * [3, 2, 2, 1], mono decrease.
    * next element is 2, and it will start the flushing.
  * [3, 2, 2, 2], Total += 1
  * [3, 2, 2, 2, 0], mono decrease.
    * Next is 3, flush is gonna start.
  * [3, 3], Total += 3 + 1 + 1 + 1

* Edge cases:
  * Mountain... this is going to cause trouble for our algorithms
  * solution: We need a dummy variable as the first element of the array to inform us that
  we are at the edge here.
  * The dummy variable does the following things:
    * stop the flushing, clear the accumulating water.
  * OR: when a element flushes all the way until the stack becomes empty, it will lose all the waters it tries to
  trap.

* **The above algorithm is incorrect**
  * This algorithm is correct by consider the following:

  ```
    # # # # *
    * * # # *
    * * * # *
    * * * * *
  ```

  * It computes more area than we needed for the problem.


## Idea 2

* Flushing but count the whole area and them minus the bars in side... yeah... let's do the above one and flush it
to see how this shit works out.

* No, it failed because it didn't count some of the water block in the middle of the valley.

## Ok I failed, Let's reveal the thing here

* Brute force:
  * for each bar, look for the maximum among all the bars to the left of the current bar, and the minimum among all
  the baron hte right of the bar.

  * Then the height of the water above the current bar is gonna be: `min(left_max, right_max) - height`, where height
  is the height of the current bar.

  * The recursion can be summarized by the following:
    * Let `H` be the array of integers representing the height of bars in the array.

  ```
    Water := 0
    I = from 0 to len(H) - 1 by 1:
      Water += min(
            max(H[J] for J in range(I)),
            max(H[J] for j in range(I + 1, len(J)))
          )
  ```
  * Nice and easy.

* Dynamic Programming:
  * This solution memerize the recursive part of the previous solution and reduced the complexity of the class.
  * As we flushing through from left to right of the array, we maintain the element that is maximum up until I, including
  I

  * Constructing the Left_max array using DP:
  ```
    Leftmax[-1] := 0
    for I := from 0 to len(H) - 1 by 1:
        Leftmax[I] := max(Leftmax[I - 1], H[I])
  ```
  * The same pattern holds for constructing the Rightmax for the problem.

* 2 Pointer:
  * This is just an improvement to the DP routine, and here is the java solution:

  ```java
        public int trap(int[] height) {
            if (height == null || height.length == 0) return 0;
            int l = 0,
            r = height.length - 1,
            level = 0,
            current = 0,
            res = 0;
            while (l < r)
            {
                if (Math.min(height[l], height[r]) > level)
                {
                    level = Math.min(height[l], height[r]);
                }
                if (height[l] <= height[r])
                {
                    current = l++;
                }
                else
                {
                    current = r--;
                }
                res += level - height[current];
            }
            return res;
        }
  ```

  * This idea so far is the coolest and craziest.

  * **What is 2 Pointer Exploiting?**
    
    * The 2 point is exploiting the fact that, one of the point is always climbing up, and this forms the basis
    for us to trap more and more water between these 2 pointer, and it can also be visualized as light shooting from
    both side of the array, from left and to the right, and we are searching for the area of the shadows.

* Stack:

  * The stack is used to search of the element that is immediately larger than the current element to the right side
  of the current element, which can be used to calculate the volumn of the water.

  * The key I am mising here, is that, in order to trap rain water, we will need 3 bars to do that, and this is the
  part that is important.
    * The bar that is curring looking.
    * The bar that is taken out right after the flushing start.
    * The bar that is still on the top of the stack
      * If the stack only has one bar, then the water cannot be trapped.

  * Algorithm:
    ```
      Given: Height  # The height of the bars in the array.
      Initialize Stack = []  # Monotonical, storing bars, in differeht places in the array, strictly decreasing
      Ans = 0  # The water that got trapped.
      foreach (H: bar height, I: Bar index in the array):
        while (Stack is not empty and H > Height[Stack[-1]]):
          Top = Stack.pop()
          Width = I - Stack[-1] - 1
          BoundHeight = min(Height[Top], Height[-1]) - Height[Top] #  might need dummy variables, height can be empty.
          Ans += Distance * BoundedHeight
        Stack.append(I)
    ```

  * Let's consider a base case, and for the base case, we need at least 3 bars to trap the water.
    *
    ```
      *   *
      *   *
      *   *
      *   *
      * * *
    ```
    * The amount of water that can be trapped here is the (min(left, right) - middle)*width
  * Now let's consider the case of Valley with monotone structure.
    *
    ```
      *         *
      * *       *
      * * *     *
      * * * * * *
    ```
    *

## Some Input Examples for checking the algorithm

```
 *   *   *   *
 *   *   *   *
 * * * * *   *
 * * * * * * *
```
* `[4, 2, 4, 2, 4, 1, 4]`
* Water volumn: 7
```
                  *
* *       *   * * *
* *     * * * * * *
* *   * * * * * * *
* * * * * * * * * *
```
* `[4, 4, 1, 2, 3, 4, 3, 4, 4, 5]`
* Water: 7

## The Problem Expanded

* The problem can be expanded pretty easily, and one of the most straight forward way to do it is make
it into 3d.

* The dynamic programming solutin will still stand strong for this problem, we but this time we need to look
into all 4 direction to look for the `Level height` (Whehter there eixsts a boundary that can hold the water on that
direction).