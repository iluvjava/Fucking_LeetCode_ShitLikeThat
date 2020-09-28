# Problem Statement
* [Original Leetcode](https://leetcode.com/problems/validate-stack-sequences/)
	* This problem is relavant to: GOOGLE

* Give to lists of integers. 
	* Popped; 
	* Pushed;

* Determine if there exists a sequence of operations such that, all elements in the `pushed` sequence are pushed into the stack in order as they are in `pushed`, and all elements in the `popped` sequence are popped from the stac in the order they are in the sequence.
* Good News: 
	* All the elements involved in the pushed, and popped are unique. 

### An Example

```
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

```
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

```
### Brain Storming
* I don't think there are better way than just making an algorithm that cleverly pop, push elements from the inputs, and assess the conditions, it's like doing an experiement. 

```
	Intialize: TestStack
	while(pushed is not empty):
		push element into the stack
		if (first element of popped is the top of the stack)
			pop the stack
	
	if non of the input queus are emtpy
		return false
	return true		
```

