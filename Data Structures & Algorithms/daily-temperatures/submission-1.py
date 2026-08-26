class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ret = [0] * len(temperatures)
        for i in range(len(temperatures)) :
            while len(stack) != 0 and stack[-1][0] < temperatures[i] :
                index = stack.pop()[1]
                ret[index] = (i - index)
            stack += [(temperatures[i], i)]
        return ret
            

