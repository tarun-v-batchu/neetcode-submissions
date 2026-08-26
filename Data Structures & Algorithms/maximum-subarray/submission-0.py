class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_max = nums[0]
        running_max = 0
        for i in nums :
            running_max = max(i, running_max + i)
            curr_max = max(curr_max, running_max)
            
        return curr_max

