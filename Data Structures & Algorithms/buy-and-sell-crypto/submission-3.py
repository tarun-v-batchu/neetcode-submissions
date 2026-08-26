class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        stack = []
        profit = 0
        
        for i in prices :
            if len(stack) == 0 or stack[-1] < i :
                stack += [i]
            else :
                profit = max(profit, stack[-1] - stack[0])
                while len(stack) != 0 and i < stack[-1] :
                    stack.pop(len(stack) - 1)
                stack += [i]

        if len(stack) == 0 :
            return profit
        return max(profit, stack[-1] - stack[0])
