def decompress(s):
    Counter = 0
    UnCompressedString = ""  # part of our results
    TheNumber = ""
    TheMap = {}  # maps the number to the expression
    I = 0
    while I < len(s):
        if s[I].isdigit():
            TheNumber += s[I]
        elif s[I] == "[":
            BracketCount = 1
            I += 1
            Expression = ""
            while I < len(s) and BracketCount != 0:
                Expression += s[I]
                if s[I] == "[":
                    BracketCount += 1
                elif s[I] == "]":
                    BracketCount += -1
                I += 1
            # Recursion here. 
            UnCompressedString += int(TheNumber) * decompress(Expression[:-1])
            TheNumber = Expression = ""
            continue
        else:
            UnCompressedString += s[I]
        I += 1
    return UnCompressedString


def print_nested_brackets(n=7):
    if n == 0:
        return ""
    return "[" + print_nested_brackets(n - 1) + "]"


def main():
    print(print_nested_brackets())
    print(decompress("u2[4[asdf]]"))
    print(decompress("x2[b5[c]4[y]]"))
    print(decompress("x2[y2[a2[q4[t]]]]"))
    pass

if __name__ == "__main__":
    main()