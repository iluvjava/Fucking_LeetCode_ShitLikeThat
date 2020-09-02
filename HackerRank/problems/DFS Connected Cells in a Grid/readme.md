# Problem Statement

* [link](https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs)


* Find maximum size of the maximum connected region.

* Adjacent means: Horizontal, Vertical, and Diagonal. 

* Connected:
  * All of them clustered together.

## Idea 1 (Failed)

* Dynamic programming.
  * T[I, J] := "The size of the blob of region that located at the bottom right corner at index [I, J]"

* Recurrence:
  * T[I, J] := max(T[I - 1, J - 1], T[I - 1, J], T[I, J - 1]) + 1

* This idea doesn't work, consider the following:
  * 
  ```
    1 0 0 1
    0 1 1 0
    0 0 0 0
    0 0 0 0
  ```

## Idea 2: DFS

* Just do a DFS and find the size of the connected components and that is all. 
