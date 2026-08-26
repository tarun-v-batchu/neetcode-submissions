class Solution:
    def jump(self, nums: List[int]) -> int:
        
        i = len(nums) - 2
        arr = [100000] * len(nums)
        arr[-1] = 0
        while i >= 0 :
            boo = 100000
            # print(arr)
            for j in range(i, min(i + nums[i] + 1, len(arr))) :
                # print(boo, j, arr[j])
                boo = min(boo, arr[j])
            arr[i] = boo + 1
            i -= 1
        # print(arr)
        return arr[0]

