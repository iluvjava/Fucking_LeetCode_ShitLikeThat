def solution(h):
    """
        Given list if integers representing the height of the bars, 
        we want the maximmum size of the rectangle that is hiddden in the bar chart. 
    """
    Stack = []
    RunningMax = 0
    for I in range(len(h)):
        if len(Stack) == 0 or (h[I] >= h[Stack[-1]]):
            Stack.append(I)
        else:
            Counter = 1
            while len(Stack) > 0:
                Height = h[Stack.pop()]
                RunningMax = max(RunningMax, Height * Counter)
                Counter += 1
            Stack.append(I)
    return RunningMax


def largestRectangleArea(A):
    ans = 0
    A = [-1] + A  # This is playing around with the index too.
    A.append(-1)  # Very interesting, ver smart. 
    n = len(A)
    stack = [0]  # store index
    for i in range(n):
        print(f"looking at: {i}, stack {stack}, {[A[I] for I in stack]}")
        while A[i] < A[stack[-1]]:
            print(f"\tEmptying Stack: {stack}, {[A[I] for I in stack]}")
            h = A[stack.pop()]
            print(f"\th: {h}; i = {i}; top: {stack[-1]}")
            area = h*(i-stack[-1]-1)
            print(f"\tarea: {area}")
            ans = max(ans, area)
        stack.append(i)
    return ans

def main():
    print(largestRectangleArea([3, 2, 3]))
    print(largestRectangleArea([6, 2, 5, 4, 5, 1, 6]))



if __name__ == " __main__":
    main()

main()

