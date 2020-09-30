## Intro
* In this section, we will focus on strategies that reduce a recursive functionn to an iterative function. 
* Note: This is complicated and it really depends on the functions we are trying to reduce and it will make use of a variety of data structures. 
* Some of the codes I am using will be in [[Code Vault]]


## A General Guide
* When we try to put a recursive function in to a iterative scheme, we need to understand that, **functions** are *problems*, and then spawn sub-problems, similar to how a recursive function calls on itself.
	* The question need to solve the problem <--> Inputs of the function
	* The answer to the problem <--> return value of the function
	* The procedures of the problem <--> contents of the function
* Each part of the function must be addressed and referenced via data structure to stackify the function.

## The Fibonacci Number
```python
def fib_recur_mem_stackified(n, T = {}):
    """
        Inner Scope Stackification of Fibo-Sequence Memiozation
    """
    if n <= 0:
        return None
    T[1] = T[2] = 1  # Important! Base Cases. 
    def F(i):
        if i in T:
            return T[i]  # Out of this means no base cases. 
        S = [i]
        while len(S) != 0:
            i = S[-1]
            # Merge in ---------------------------------------------------------
            if ((i - 1) in T) and ((i - 2) in T):
                T[i] = T[i - 1] + T[i - 2]
                S.pop()
            # Branch out -------------------------------------------------------
            else:
                if (i - 1) not in T:
                    S.append(i - 1)
                    continue
                S.append(i - 2)
                continue
        return T[i]
    return F(n)
```
* Recurrences: f(n) := f(n - 1) + f(n - 2) if n >= 2 else return 1
* In order to solve a problem f(n), we need results from f(n - 1) and f(n - 2) first to solve it, except for the case where n< 2. 
* In order to keep remebring the results from sub problem, we make a map, `T[I]:=f(I)` to store the results, for the given problem f(I).
* When we look take a look at the problem on top of the stack, and query whether the sub-problems need to solve the current element are sufficianly solved. 
	* If it's the case, then we merge the results and stored it to `T[i]` and pop `f(i)` out of the stack.
	* If that is not the case, if any one of the sub probelm is not yet in `T`, we add them in and back to the stack to retrieve the next problem to solve.

## The Ackerman Function
* This function has the same underlying principles as the fibbonacci, except that it's more complex. But it works similarly to the above fibbonacci example.
* The recurrences of the Ackerman is described as: 

$$
A(m, n) :=
\begin{cases}
	n + 1 & m = 0\\
	A(m - 1, 1) & m > 0 \wedge n = 0\\
	A(m - 1, A(m, n - 1)) & m > 0 \wedge n > 0
\end{cases}
$$

```python
def Ackerman(m, n):
    T = {}  # mem
    M, N = m, n
    Stack = [(M, N)]
    while len(Stack) != 0:
        M, N = Stack[-1]
        if M == 0:
            T[M, N] = N + 1
            Stack.pop()
            continue
        if M > 0 and N == 0:
            if (M - 1, 1) in T:
                T[M, N] = T[M - 1, 1]
                Stack.pop()
            else:
                Stack.append((M - 1, 1))
            continue
        if M > 0 and N > 0:
            if (M, N - 1) in T:
                if (M - 1, T[M, N - 1]) in T:
                    T[M, N] = T[M - 1, T[M, N - 1]]
                    Stack.pop()
                else:
                    Stack.append((M - 1, T[M, N - 1]))
                continue
            else:
                Stack.append((M, N - 1))
            continue
    return T[m, n]
```

* This function is very recursive because of the fact that, the input parameters are the out put of the sub functions.


### The General Pattern Here
* Each functoin is modeled as its input, and its output, let's call it a **problem**
* Peek the problem on the top of the stack 
	* Check if sub problems needed to solve this problems are solved (checking the memoirized results), if not add sub problem to the stack and goes back to the stack and retrieve another problem.
	* if the sub problems are solved, combine results from the sub problems and then solve the current problem. Pop current problem from the stack to indicate the problem is solved. Stored the results in a data structure for future references.


## DFS, a More Complicated Example
* [[Depth First Search]]
* When reading the example, taking notice how the iterative scheme is also keeping track of the **states** of the recursive function while doing the recursion. Each time a function calls itself, the caller instance will be freezed.