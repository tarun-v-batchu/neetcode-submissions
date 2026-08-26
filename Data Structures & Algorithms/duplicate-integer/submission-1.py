class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not len(nums) :
            return False
         
        mini = min(nums)
        maxi = max(nums)

        arr = [False] * (maxi - mini + 1)

        for i in nums :
            if arr[i - mini] :
                return True
            arr[i - mini] = True

        return False
        