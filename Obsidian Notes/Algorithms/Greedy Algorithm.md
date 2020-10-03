## Greedy algorithm 

* As the name sugguest, the algorithm choose the action from a set of actions with the following rules: 
	* Keep the solutoin feasible
	* The increment for this action is maximal


### Features
* This algorithm requires proof to show that it can produce optimal solution, unfer most cases, it doesn't. 
* This algorithm is the key to Branch and Bound algorithm, which is for solving NP-Hard problems. 
* Matroid, some Greedy Algorithm has this beautiful structure. 
* Greedy algorithm is the special case of a [[Dynamic Programming]], by which case, we only keep ONE optimal solution at hand and improve it in a greedy manner, the simpliest Dynamic Programming structure.


### How to Reason with Greedy Algorithm
* Assume an optimal solution to the problem is given, then at each step of the algorithm, prove that it's the optimal solution. 
	* Complete the proof inductively 
* At each stage of the algorithm, prove  that it stays ahead among all other possible choices. 
* Find the Invariant, connect the algorithm invariant to the optimal solution, then prove that the algorithm terminates with the invariant.


### Practices Problems

* Maximal Number of Intervals can be Scheduled: Canonical
* [[Greedy Flourist]]
* [[Reverse Shuffle Merge]]
* [[Luck Balance]]
* [[Max Min]]
* [[Minimum Absolute Difference In an Array]]
* [[Mark and Toys]]