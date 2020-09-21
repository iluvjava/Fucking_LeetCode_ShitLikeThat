# Problem

* [Problem Link](https://leetcode.com/problems/analyze-user-website-visit-pattern/)

* Given a sequences of users, website and times tamps
  * `username[i]` visited website `website[i]` at time stamp `timestamp[i]`
  * The length of each array is larger than 3 and less than 50

* note: Not users vists the same website at the same time. 
* There are maximal of 10 possible websites. (Can be exploited)

* Find: 
  * No 2 users vist the website at the same time, so for each time stamp, we get unique user and the website they are 
  visiting. 

## Idea1

* Find the sequence of website for each of the users. 

* Countruct the set of unique triplet sequences of website for each of the user.

* Merge in all possible triplets from all the users.

* For each triplets in the the set, find how many users share that triplets in their set.

* Among all the triplets, find the one with least lexical graphic order.

* This is the correct answers as shown by the Leetcode hints system. 
