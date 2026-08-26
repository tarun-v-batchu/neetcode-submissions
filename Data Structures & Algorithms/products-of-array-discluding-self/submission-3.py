class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 2 :
            return [nums[1], nums[0]]

        i = 0
        forw = []
        prod = 1
        while i < len(nums) :
            prod *= nums[i]
            forw += [prod]
            i += 1
        
        i = len(nums) - 1
        back = []
        prod = 1
        while i >= 0 :
            prod *= nums[i]
            back = [prod] + back
            i -= 1

        ret_arr = [back[1]]
        i = 1
        while i < len(back) - 1 :
            ret_arr += [forw[i - 1] * back[i + 1]]
            i += 1
        
        return ret_arr + [forw[-2]]


        