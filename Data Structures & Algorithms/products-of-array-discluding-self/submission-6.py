class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward = [1]
        for i in nums :
            forward += [i * forward[-1]]
        backward = [1]
        i = len(nums) - 1
        while i >= 0 :
            backward = [nums[i] * backward[0]] + backward
            i -= 1
        # print(forward, backward)
        
        arr = []
        i = 1
        while i < len(backward):
            arr += [forward[i - 1] * backward[i]]
            i += 1
        return arr
