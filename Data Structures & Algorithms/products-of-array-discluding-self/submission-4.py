class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1 :
            return [nums[0]]
        
        front = [nums[0]]
        i = 1
        while i < len(nums) :
            # print(nums[i])
            front += [nums[i] * front[-1]]
            i += 1
                    
        back = [nums[-1]]
        i = len(nums) - 2
        while i >= 0 :
            # print(back)
            back = [nums[i] * back[0]] + back
            i -= 1
        # print(back)
        
        # print(back, front)
        arr = [back[1]]
        for i in range(1, len(nums) - 1) :
            arr += [front[i - 1] * back[i + 1]]

        arr += [front[-2]]
        return arr



