class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            raise Error("bruh")
        
        op = tokens.pop()
        print("looking at", op)
        print(tokens)

        if op not in ['+', '-', '/', '*']:
            return int(op)
        
        print("recursing")
        print("left")
        r = self.evalRPN(tokens)
        print("right")
        l = self.evalRPN(tokens)

        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        elif op == '/':
            return int(l / r)