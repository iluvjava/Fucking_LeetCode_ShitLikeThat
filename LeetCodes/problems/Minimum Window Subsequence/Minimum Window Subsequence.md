# Problem Statement

* Given a string and a sequence, find the minimum continguous substring containing such a subsequence.
* This problem is asked by GOOGLE.

## Approaches (Failed)

* This is a dynamic programming problem.

* Given a string `S` that current containing the sequence `T`. Consider a new added character `c` to the string `S`

* Suppose withold the following knowledge about the sequence and the subsequence. 
	* If we start at index `I`, what is the minimum length needs to contain `T` in `S`.
		* `inf` if it's just impossible
		* `k` the length need to go further to get a contiguous full substring containing the `T` sequence.
	* If we start at index `I` and go back, what is the minimum length to cntain the `T` in the subsequence? 
		* `inf` if it's just impossible 
		* `m` the length need to go back to
	* Ok, they are essentially the same thing, just different indices and directions and such.

* This is not useful, we need more than just the number, or a true or false statement. 

* How much of the subsequence `T` we can get from `S` from index `I` to `J` inclusive? 
	* say the subsequence we want is: `abcde`
	* and we are looking at `aabfcidffg`, and then the cloest thing we can get from it into `abcde` is `abcd`. 


## Approaches (Look to The Left)
* Given `I` and `J`, how much further back I need to go from `I` and goes back so that `S[I - k:I + 1]` contains the sequence `T[:J + 1]`
* Denote that that `Opt[I, J] = k`
* Let's fixed the index `I`, `J` on the string `S`, `T`, then there are the following cases:
	* If `S[I] == T[J]`
		* Then `Opt[I, J] = Opt[I - 1, J - 1] + 1`
	* else
		* `Opt[I, J] = T[I - 1, J]` 
		* By including the new character from the subsequence, and search one index in advance in `S` for the smallest index containing the sub-sequence. 

* Let's say that `S = abcdfe`
	* We are interested in `T = abcde`
	```
		a  b  c  d  f  e
	a	0  1  2  3  4  5 
	b   *  1  2  3  4  5
	c   *  *  2  3  4  5
	d   *  *  *  3  4  5
	e   *  *  *  *  *  5

	```
	* `*` is positive infinity
	* And that is the compute table `opt[I, J]`, where `I` goes cross the row, and `J` goes cross the columns, and `Opt[I, J]` is the "Minimum number of indices to go back such that `S[I - k, I + 1]` contains `T[:J + 1]` as a subsequence."

* Now let's start talking about the base cases 
	* `Opt[I, 0]` := minimum k to go back on string `S` so that letter `T[0]` is equal to `S[I - k]`
	* `Opt[1, J > 0]` := `inf` 
		* There is no way, we can includes the subsequence more than 2 letters using only one letter. 

* This solution time limit exceed on leetcode submission. 


### Improvements
* Notice that we can use one array instead of using 2 of them to save some memory for the algorithm. 
* Instead of storing the: "Smallest index to go back", stores: "The largest index to the left of the current index in Opt"

## A Better Recurrence (Remebers the Index)
* `DP[I, J]:= ` the maximal index such that `S[DP[I, J]: I + 1]` contains the subsequnce `T[:J + 1]`. 
* Let's fix `I`, `J` to be in `T`, and `S` (different from last time)
	* if `T[I] == S[J]`:
		* Then this is match
		* `DP[I, J] = DP[I - 1, J - 1]`
	* else:
		* It's not a match
		* `DP[I, J] = DP[I, J - 1]`
		* Let's try to contain the whole subsequence of `T[:J + 1]` starting off with `J - 1` in S, and then add one to that window on the string. 
* So, simply phrased, it's gonna be: 
	* `DP[I, J] = DP[I - 1, J - 1] if T[I] == S[J] else T[I, J - 1]` 
* Or using On array
	* `DP[I] := DP_Old[I - 1] if T[I] == S[J] else T[I]`

* Let's try to do that on the compute table: 
	```
		a  b  c  d  f  e
	a	0  0  0  0  0  0
	b   *  0  0  0  0  0
	c   *  *  0  0  0  0
	d   *  *  *  0  0  0
	e   *  *  *  *  *  0
	```
* Note: `I` goes vertically while `J` goes horizontally. 
* `*` denotes that, `S[:I + 1]` doesn't not contain the substring `T[: J + 1]`


```
	m  -  m
m   0  0  2
m   *  *  0
```


## A new Point of View
* Instead of looking to the left, we can also choose to look to the right on the array. 

## What we Learn

* Notice that, the **first occurence of some character to the left** such that it's a certain character can also be computed with dynamic programming to save some amount of times too. 
	* The first row of the compute table is an example of that.






