class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward = [nums[0]]
        for i in nums[1:] :
            forward.append(i * forward[-1])
        backward = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1) :
            backward.append(nums[i] * backward[-1])
        
        # print(forward, backward)
        final = [backward[-2]]
        for i in range(1, len(nums) - 1) :
            final.append(forward[i - 1] * backward[len(nums) - 1 - (i + 1)])
        
        final.append(forward[-2])
        return final


