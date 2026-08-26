class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1 :
            return nums[0]
    
        arr = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums) :
            arr += [max(arr[i - 1], arr[i - 2] + nums[i])]
            i += 1

        return max(arr[-2], arr[-1])