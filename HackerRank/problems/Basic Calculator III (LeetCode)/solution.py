def solution(s):
    
    s = parse_string(s)
    
    def EvalNoBrackets(i, j):
        """
            i, J both inclusive
        """
        Stack1, Stack2 = [], []
        for I in range(i, j + 1):
            
            print(Stack1, Stack2)
            
            Token = s[I]
            if type(Token) != int:
                
                while len(Stack2) != 0 and OptRank(Token) > OptRank(Stack2[-1]):
                    T1 = Stack1.pop(); T2 = Stack1.pop()
                    Opt = Stack2.pop()
                    Stack1.append(compute(T1, T2, Opt))

                Stack2.append(Token)
            else:
                Stack1.append(Token) 
        
        while len(Stack1) != 1:
            T2 = Stack1.pop(); T1 = Stack1.pop()
            Opt = Stack2.pop()
            Stack1.append(compute(T2, T1, Opt))
            
            print(Stack1, Stack2)

        return Stack1[0]

    def OptRank(opt):
        if opt in "+-":
            return 2
        if opt in "*/":
            return 1
        return None

    def compute(a, b, opt):
        if opt == "+":
            return a + b
        elif opt == "-":
            return a - b
        elif opt == "*":
            return a * b
        elif opt == "/":
            return a//b
    
    def HasBrackets(i, j):
        pass
    
    return EvalNoBrackets(0, len(s) - 1)


def parse_string(s):
    Token = ""
    Tokens = []
    for C in s: 
        if C not in "+-*/":
            Token += C
        else:
            Tokens.append(Token)
            Tokens.append(C)
            Token = ""
    Tokens.append(Token)
    return list(reversed([(int(T) if T not in "+-*/" else T) for T in Tokens]))


def main():
    solution("3 + 8 * 7 / 2")
    solution("6 - 4 * 6 + 9 - 3 / 3")
    solution("3*5/6-4+2")



if __name__ == "__main__":
    main()
