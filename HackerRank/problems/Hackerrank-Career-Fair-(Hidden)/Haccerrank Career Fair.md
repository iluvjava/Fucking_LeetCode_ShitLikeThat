* Rotating a string from left to right, circular, how many of them will produce a string such that. 
the first and the last letter are the same.

* An array of integers are given to represents the sizes of boxes, and a box that half the size of another box 
can be put into the larger box, and only one box can be put into the other box. 
  * No deep nesting, only one box can be inside another box, and the is no other box can be nested inside anymore a
  after that point.

    * I have no idea how to solve this except for using brutefoce recursive solution to the problem. 


* Given a set of intergers, and another integer, say k.
  
  * distribute the number k into integers in the array by adding it to integers in the 
  array, maximizing the number of same number of integers.

  * For this problem, I believe we need to make an muti-set out of the differences for the intergers in the array,
  after sorting the `arr`. Then we are doing this in a greedy manner, and then we try to distribute the number 
  between groups to get the as even as possible. 

  * [4, 5, 4, 4, 5, 4], sorting it to get [4, 4, 4, 4, 5, 5]
  * And then we take the elemewise difference between the element, which should give:
    * `[0, 0, 0, -1, 0]`
    * which is useless. 
    * Let's make a sorted multiset out of the elements: 
      * [4: 4, 5: 2]
      * adding 1 to 4 will migrate the element from bucket to bucket. 
      * Iterate through the multi-set, and then find the minimum difference between the key, and then try to fill 
      in with the integer k. Do that for several iteration until:
        * Runs out of integer k
        * or all of the differences in keys are larger than k. 
      * Remember to delete the key after they are exhausted. 


  