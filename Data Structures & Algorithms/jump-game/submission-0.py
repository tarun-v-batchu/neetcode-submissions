class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = len(nums) - 2
        arr = [False] * len(nums)
        arr[-1] = True
        while i >= 0 :
            boo = False
            for j in range(i, min(i + nums[i] + 1, len(arr))) :
                boo |= arr[j]
            arr[i] = boo
            i -= 1
        # print(arr)
        return arr[0]

