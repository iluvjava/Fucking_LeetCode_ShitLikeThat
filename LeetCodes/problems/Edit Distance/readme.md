## Edit Distance Problem Statement

* Each of the operations performed on word has a cost of 1
  * Insert a char
  * Delete a char
  * Replace a char

* Delete + Insert ==> Replace

* (Link)[https://leetcode.com/problems/edit-distance/]

## Review: The String Alignment Algorithm (Failed)

* a = "stops", b = "tops"

* Final alignment: stops == ~tops

```python
  s t o p s
t - * 
o     *
p       *
s         *
```

* INSERTING into a
```python
  g
g *
g +
g +
g +
```

```python
word1 = "horse", word2 = "ros"
  h o r s e
r 1 2 2 3 4
o 2 2 3 3 4
s 2 3 3 3 4

  h o r s e
r 1
o   1
s     2 2 3

  i n t e n t i o n
e 1 2 3 3 4 5 6 7 8
x   2
e     3
c       4
u         5
t           5
i             5
o               5
n                 5

  a b c d e
a 0 1 2 3 4
```

* Notice: Insertion into  `a` is a deletion for `b`

* That is where the optimal path on the compute table.

## Idea (The Optimal Path and Decision we make on the compute table)

* T[I, J]: "Minimum cost for editing sub-string a[: I + 1], b[:J + 1]"

* T[I, J] := T[I - 1, J - 1] + 1 if MISMATCH 0 if MATCHED
  * The cost of replacement is included in `1` in the expression.

* T[I, J] := T[I - 1, J] + 1 if MATCHED else 0
  * Deleting `a[i]` or inserting matching letter for at `i` of b.

* T[I, J] := T[I, J - 1] + 1 if MATCHED else 0
  * Inserting at `b[i]` or deleting letter from `a[i]`

* Base cases?
  * No, don't use "+inf", that will pollute the arithematic. 
  * Use 0 means no edits. 




"zoologicoarchaeologist"
"zoologicoarchaeologist"
"zoo~~g~~~~~~~~eologist"


```
  s e a
e 1 1 2
a 2 2 1
t 3   2
```

* Diagonal Direction is all good, but the... the... Vertical and Horizontal needs working and polishing. 

## Just read From Geek for Geek and solve it. 