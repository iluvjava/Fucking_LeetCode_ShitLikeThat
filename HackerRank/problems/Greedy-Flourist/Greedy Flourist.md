# Identifying Information from the Problem Statement

* [link](https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms)

* For each flowered purchased by the customer, the price of the flower is (k + 1) where k is the number of flowers
that the customer has previously purchased.
  * the k th flower purchased by the customer is: (k + 1)*(P: Price of the flower.)

* Example:
  * Prices of flowers want to by: [1, 2, 3, 4]
  * Numer of people buying the flowers: 3
  * Solution:
    * First 3 people buy: [2, 3, 4]
    * Last people buy: [1]

## Identify the problem type and forge the correct approach to the problem

* If the prices for all the flowers that we want to buy is the same, then we have to spread out
the purchases to each of the person in the group.

  * Assuming this is not the case, that, one person didn't buy any flower is purchased by other,
  then, compare to the case where the purchase is made by the person who bought that flower, which
  improved the optimality of the solution.

* Assume we only have one person, and the prices of the flower is: [1, 2, 3, 4]

  * then the best strategy is to buy them in descending order: [4, 3, 2, 1].
    * `[4 + 3*2 + 2*3 + 1*4] = 20`
  * Any other order will increase the price. (A swapping argument will show that)

* Now, for multiple people, it's the same:
  * Let the price of the flowers to be in decreasing order.
  * Divide the flowers into K - groups. `[[size: k], [size: k],... ,[size <=k]]`
  * Then, each group of purchase will be the kth purchases for each person in the group.
  * buying the flowers in this manner should produce the minimum costs of buying the flowers.

## Algorithm and how to code this shit

* Prices of the the flowers sorted into descending order.

* Divides them into "k" groups.

* Foreach(Group in the prices of flowers in descending order, I: As an running index for the loop):
  * Accumate: [(I + 1)*sum("prices of flowers in that group")] to a running sum.

* Yep, that algorithm is indeed the correct solution to the problem.
