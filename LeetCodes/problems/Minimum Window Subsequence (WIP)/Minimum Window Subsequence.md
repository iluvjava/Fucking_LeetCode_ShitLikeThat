# Problem Statement

* Given a string and a sequence, find the minimum continguous substring containing such a subsequence.

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


## Approaches: 
* Given `I` and `J`, how much further back I need to go from `I` and goes back so that `S[I - k:I + 1]` contains the sequence `T[:J + 1]`
* Denote that that `Opt[I, J] = k`
* Let's fixed the index `I`, `J` on the string `S`, `T`, then there are the following cases: 
	* If `S[I] == T[J]`
		* Then `Opt[I, J] = Opt[I - 1, J - 1] + 1`
	* else
		* `Opt[I, J] = min(Opt[I, J - 1] + 1, Opt[I - 1, J] + 1)`

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



