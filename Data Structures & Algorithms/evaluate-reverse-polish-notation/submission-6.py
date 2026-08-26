class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens :
            # print(i, stack)
            if i in ["+", "-", "/", "*"] :
                second = stack.pop()
                first = stack.pop()
                
                if i == "+" :
                    stack += [first + second]
                elif i == "-" :
                    stack += [first - second]
                elif i == "*" :
                    stack += [first * second]
                elif i == "/" :
                    if first // second < 0:
                        stack += [(first+(-first%second))//second]
                    else :
                        stack += [first // second]
                    # print(stack)
            else :
                stack += [int(i)]
        
        return int(stack[0])
            
