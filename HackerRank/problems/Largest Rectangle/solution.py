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


def main():
    pass


if __name__ == " __main__":
    main()