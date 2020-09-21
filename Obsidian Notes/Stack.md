## The Stack Data Structure

* Last in First out, this is the feature that got widely used, and it's the only feature the stack has. 

* It's used for [[Depth First Search]]

* The stack data structure gives quick reference to the most recent element being added to the stack, which is always used. 
	* [[Alternating Characters]]


## Keeping a Monotonic Sequence
* This exploit of the stack data structure is one of the most insane, and hardest one too. 
	* By keeping a monotonic sequence in the stack, we are able to identify for each element, the element that is immediately larger/smaller (larger or equal to/ smaller or equal to) in the array. Which is featured in the [[Min Max Riddle]]
	* While keeping the invariant in the stack, we pop element out and compare the index in the array of the current element and the element popped out, which is exploited via these following problem: 
		* [[Max Retangle]], Which is asking us to determine the rectangle with the largest area in the graph.
		* [[Trapping-Rain-Water]]