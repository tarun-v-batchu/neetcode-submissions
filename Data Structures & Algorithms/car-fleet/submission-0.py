class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = sorted([(p,s) for p, s in zip(position, speed)], reverse=True)
        stack = []
        fleet = 0
        print(arr)
        for p, s in arr :
            end_pos = (target - p)/s
            stack.append(end_pos)
            if len(stack) >= 2 and stack[-1] <= stack[-2] :
                stack.pop()
            
        return len(stack)
