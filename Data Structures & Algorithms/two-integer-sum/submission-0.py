class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = {}

        for i in range(len(nums)) :
            if target - nums[i] in table :
                return [min(i, table[target - nums[i]]), max(i, table[target - nums[i]])]
            table[nums[i]] = i
        
        return [-1,-1]