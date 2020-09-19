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
  * 