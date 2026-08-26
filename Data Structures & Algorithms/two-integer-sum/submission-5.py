class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for index, i in enumerate(nums) :
            if target - i in m :
                return [m[target - i], index]
            m[i] = index
        return [0, 1]