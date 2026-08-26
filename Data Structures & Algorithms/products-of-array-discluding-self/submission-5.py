class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1, 2, 4, 6]

        # forward: [1, 2, 8, 48]
        # backward: [48, 48, 24, 6]

        forward = [nums[0]]
        i = 1
        while i < len(nums) :
            forward += [forward[-1] * nums[i]]
            i += 1
        
        backward = [nums[-1]]
        i = len(nums) - 2
        while i >= 0 :
            backward = [nums[i] * backward[0]] + backward
            i -= 1
        
        final = [backward[1]]
        i = 1
        while i < len(nums) - 1 :
            final += [forward[i - 1] * backward[i + 1]]
            i += 1
        
        final += [forward[-2]]

        return final



