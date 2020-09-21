# Problem Statement

* Give a list of words, **Without Repeatitions**, return all the words, W, satisfying the follwoing condition:
  * It can be concatenated using words that are from the same set.

## Using the Hashmap Set/Inverse Frequency Map Repeatedly

* For each words, we know that it is possible that it's made with words with smaller length in the set.
  * if this is the case, we try to focus on the length of the words, of 2 or more multiple words sum up to the same
  length to the word we are currently looking at, then, that is the set of words we want to seach through.

* Say we have a map that is maping from the length of the words to a list of words that is in the set.

* I choose an word in the set, for all the integer: `L` such that `L` is less than the length of the world, I search
among all the words with length `len(word) - L`, and then I add the words to it, and then we do this `Recursively`,
on the partially constructed words.

## Is there a Dynamic Programming Shit Behind This?

* Yes, once we constructed a composite word, we included that back to the hash set, which might become the components
for an even longer word.

* The codes:
  * bleh... I am still thinking about it.

