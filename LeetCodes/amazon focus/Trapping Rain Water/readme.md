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

* Stack:
  * The stack is used to search of the element that is immediately larger than the current element to the right side
  of the current element, which can be used to calculate the volumn of the water.
