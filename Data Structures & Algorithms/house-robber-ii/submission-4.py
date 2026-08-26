class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(nums) :
            if len(nums) == 0 :
                return 0
            if len(nums) == 1 :
                return nums[0]
            list = [0] * (len(nums))
            list[0] = nums[0]
            list[1] = max(nums[0], nums[1])
            i = 2
            while i < len(nums):
                list[i] = max(list[i - 1], list[i - 2] + nums[i])
                i += 1
            return list[-1]
        if len(nums) == 0 :
            return 0
        if len(nums) == 1 :
            return nums[0]
        max_one = house_robber(nums[:len(nums) - 1])
        max_two = house_robber(nums[1:])
        
        return max(max_one, max_two)