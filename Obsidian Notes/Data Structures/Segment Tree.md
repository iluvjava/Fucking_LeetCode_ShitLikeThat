The Segment Tree: 
1. Efficiently handle queries about partial sums. 
2. Flexibily modifying the entries inside of the array. 
References and Resources: [CP-Algorithms Seg Tree](https://cp-algorithms.com/data_structures/segment_tree.html)
---
### Intro

The tree will answer the questions about the partial sum, summing from the beginning of the array to an certain index k efficiently and it allows for modifications of the elements in the array one at the time. 

### The Tree

This is the definition. 

1. The root of the node represents the partial sum from k to l. Then the left and right parents represent the: 
	* Left half sum of that partial array. 
	* Right half sum of that partial array. 

Let's take a look at the example tree for the array: `[1, 3, -2, 8, -7]`

![[Seg-tree.png]]

And notice that base case is referencing to one single elements in the array, and that is the smallest possible unit. 

**Note:**  In this example, the tree is a full, regular binary tree, does this has anything meaningful? Like for the implementations if this is hold for all sizes of arrays? 

Now let's see how this tree will help us with the operations. 
1. Query any partial sum on the tree. 
2. Change an element while keeping the invariant of the tree. 

##### Sum Queries: 

If the current node is representing the interval $I$ and it's left and right child represents the interval $I_L$, $I_R$, and the inverval we want to sum up is $M$, and $M\subseteq I$ then there are the following cases: 
1. $M = I$, return the sum that is written in this node. 
2. $M \subseteq I_L \dot\vee M\subseteq I_R$, then go to that node and recur. 
3. if $I_L\subseteq M \wedge I_R \subseteq M$, then split $M$ into 2 intervals $M_1, M_2$ such that $M_1\dot\cup M_2 = M$ and $M_1\subseteq I_L \wedge M_2\subseteq I_R$, and then recur with $M:=M_1$ for left child, then recur for $M:=M_2$ for right child, and then sum them after what has been returned by the recursion. 


Ok, so this shit recurs differently depending on what the interval is on the node. How can we make sure that it won't recurs for the whole tree? 

Let's say it recur for the whole tree, then it's summing up all the node, then it's a full interval, then it should be stopped at the root node, **Contradictions**. 

Let's say at some point of the recursion, more than 4 nodes are visited at a certain level. Then it must be the case that, the interval is matching the common ancester of all those 4 nodes OR the common ancester of those 4+ nodes are having an interval that is less than the given interval, this is a contradictions to the algorithm. 

Therefore, we can assure you that, at most 4 nodes will be visited at any level of the tree whenever a query is made. 

This is a constant, and the depth of the tree is going to be bounded by $\mathcal{O}(\log(N))$ and then therefore, this query is going to cost us $\mathcal{O}(\log{N})$. 


### Updating An Elements


Let's assume that the element we are going to up date is $a$, and the current node is representing the sum for interval $I$ with left and right children representing the interval: $I_L$ and $I_R$, then the algorithm runs recursively by the following: 

**Part I: Reach to the Bottom Recursively**
1. If the current node $I$ is root node, meaning that the $I$ is a singleton, then it must be the case that $I =\{a\}$, then we update the sum of the node, and then we recurse up, go to part II. 
2. If $a\in I_L$, go to left node and recur. 
3. if $a\in I_R$ go to right node and recur.

**Part II: Reach Back to the Top and Update it**

1. For current node that is not a leaf node, update the sum accroding to the node that the algorithm recurs from. 
2. End when the current node is the root node of the tree. 


---
### Implementations

**Creating an Arary To Represents the Full Binary Tree**

We use an array that is 2 times the size of any given data array, and then we use that array as an implicit representation for our regular binary tree. 

Ok, why is this 2 times the wideth of the given data array? 

There is extra room here, but it's definitely more nodes than the length fo the array, in the case of 2 elements, a full tree of 7 nodes are used to represents it. And hence, it's making sense to have 2n as lenghth for the array that implements the tree. 

The root node of the tree is at index 1, and then it's children are at 1, 3... 

It's **the same as the implementations for the Binary Heap**. 

---
### Augmentations 

In additions to storing the sum on the node, one can also choose to store the MIN, MAX element over that interval. 

So, it's basically efficienlty finding the out put of some kind of functions that takes in a continous sub-array of an given array and split out a single output. 

Here are some of the functions that is comaptible with the Segment tree: 
1. Sum 
2. Min
3. Max
4. GCM
5. GCD

In addition, we have the choice to make 2d segment trees as well. 

---
### Applications
A lot, in competitive programming and other scenarios, like storing a CDF given a PDF discrete functions, these 2 are the immeidate thing that I can think of. 


