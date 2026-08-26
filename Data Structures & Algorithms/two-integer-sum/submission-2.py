class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = defaultdict(int)

        for i in range(len(nums)) :
            # print(target - nums[i])
            if target - nums[i] in table :
                return [table[target - nums[i]], i]
            table[nums[i]] = i
            # print(table)
        return [-1, -1]