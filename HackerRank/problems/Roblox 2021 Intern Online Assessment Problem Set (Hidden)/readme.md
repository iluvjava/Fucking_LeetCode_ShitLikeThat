## Competitive Gaming (Application of Frequencies Mapping)

* When the plahyer have the same score, they will be ranked the same, but it will affect players that
comes after it in terms of the scores.

* [100, 50, 50, 25]
* [1, 2, 2, 4]

* [20, 40, 60, 80, 100]
* [5, 4, 3, 2, 1]

### Problem Description

* Given an array of integers (The scores of the player for this round of game), and a threshold of a rank.
we want to know the maximal number of candidates that can be included for the next round of the game, player with
zero score cannot go to the next round.

* Rank: for repeated scores, the rank is defined to be the number of players that has lower scored than current player,
**NOT** including the player with the same scores from the game.

* Some kind of Sorted map is what we desired, but in this case, we can use python since we don't need frequent
modifications to the sorted map structure for the problem.

* Creates a frequencies map for all the scores in the array, name it `Freq`, Let the set of scores given by the problem
be a sorted array of integers.
  * Keep: CurrentRanks = 0, what is the current rank of the person we are looking at right now?
  * Keep: PeoplePassed = 0, This is the running sum that sums up all the number of people that got passed because
  their rank is good enough.
  ```
    while (CurrentRanks < k) let S be the score of the people from the sorted array, S will be sequencially
    incrementing:
        PoeplePassed += Freq[S]
        CurrentRanks += Freq[S]
  ```
  * Observe that the whileloop is strictly less than k, this will be key to solving the problem properly.

## University Career Fair (Greedy Interval Scheduling Problem)

* Sort all the intervals according to their end time.

* Interested in the total numbers of intervals that can be shosen in the end.

* Take notice that, 2 consequetive events can end and then start at the same time.

* If you know the greedy algorithm for finding the maximal number of unconflicted intervals, then this problem is
good, else, you might need to work from somewhere to reach the soltuion.

## Word Compression (Haven't Met it yet)

* Given a string of characters and an integer k.

* Remove sequences of repeating characters, k times, concate the string back and then repeat the process.

* Return the final word after such operations.

* Idea: Frequencies Tuple mapping for each of the characters in the string.

* **Yeah it will be good if we can use the dubugger and the testcases run faster.**

* The problem is concerned with a technique of string reduction.
  * String reducton: converting the string to a list of tuples, where each tuples repsents a sequence of consequtive
  repeating characters from the string. Tuple: (character, frequencies)

  * Data structure Invariant: The tuples that are right next to each other has to be unique.

  * This is the basis for the editing operations define by the problem in this questions, we remove sequences of]
  consequtive symbols repeated while keeping this invariant of the `Tuple List`.
