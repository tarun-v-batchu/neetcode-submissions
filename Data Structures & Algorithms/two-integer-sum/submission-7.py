class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        for index, i in enumerate(nums) :
            if target - i in dic :
                return [dic[target - i], index]
            dic[i] = index
        return [-1, -1]