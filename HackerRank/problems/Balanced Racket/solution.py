def solution(s):
    Stack = []
    Close, Open = ")]}", "([{"
    Group = {"(": 1, ")": 1, "[": 2, "]": 2, "{": 3, "}": 3}
    for C in s:
        if len(Stack) == 0:
            if C in Close:
                return False
            else:
                Stack.append(C)
                
        else:
            TopElement = Stack[-1]
            if C in Close and TopElement in Open:
                if Group[C] != Group[TopElement]:
                    return False
                else:
                    Stack.pop()
            else:
                Stack.append(C)
        #  print(Stack)
    return len(Stack) == 0


def main():
    print(solution("{{[[(())]]}}"))
    print(solution("{[()()][()[()]()]}"))

    pass


if __name__ == "__main__":
    main()