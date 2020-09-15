def solution(s):

    def parse_string(s):
        """
            Parse the string into a list of eoperands and operators. 
        """
        s = [C for C in s if C != " "]
        Operators = "+-*/()"
        Token = ""
        Tokens = []
        for C in s: 
            if C not in Operators:
                Token += C
            else:
                if Token != "":
                    Tokens.append(Token)
                Tokens.append(C)
                Token = ""
        if Token != "":
            Tokens.append(Token)
        return [(int(T) if T not in Operators else T) for T in Tokens]

    def EvalNoBrackets(expr):
        """
            input is an array of operands and oprators. 
        """
        print(f"Eval no bracket: ")
        print(expr)
        expr = list(reversed(expr))

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
            
        Stack1, Stack2 = [], []
        for I in range(len(expr)):
            
            # print(Stack1, Stack2)
            
            Token = expr[I]
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
            
            # print(Stack1, Stack2)

        return Stack1[0]

    def NextBracket(expr, start):
        """
            Given the current index of the opening bracket, find the whole sub
            expression. 
        """
        assert expr[start] == "(", "Misuse."
        RunningSum = 0
        for I in range(start, len(expr)):
            if expr[I] == "(":
                RunningSum += 1
            elif expr[I] == ")":
                RunningSum -= 1
            else:
                pass
            if RunningSum == 0:
                return I
        return None

    def EvaluateWithBracket(expr):
        """
            Intput: The array, not the string. 
        """
        ExpressionNoBracket = []
        Pointer = 0
        while Pointer < len(expr):
            if expr[Pointer] == "(": 
                NextPointer = NextBracket(expr, Pointer)
                ExpressionNoBracket.append(EvaluateWithBracket(expr[Pointer + 1: NextPointer]))
                Pointer = NextPointer
            else:
                if expr[Pointer] != ")":
                    ExpressionNoBracket.append(expr[Pointer])
                Pointer += 1
        
        return EvalNoBrackets(ExpressionNoBracket)

    s = parse_string(s)
    # print(f"After Tokenization: {s}")
    return EvaluateWithBracket(s)


def main():
    # print(solution("3 + 8 * 7 / 2"))
    # print(solution("6 - 4 * 6 + 9 - 3 / 3"))
    # print(solution("3*5/6-4+2"))
    print(solution("(3*(4-1))*(4-3*2/6)+(1+1/1)"))


if __name__ == "__main__":
    main()
