class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1 :
            return nums

        prod = [1] * len(nums)
        rev = [1] * len(nums)

        i = 1
        prod[0] = nums[0]
        while i < len(nums) :
            prod[i] = prod[i-1] * nums[i]
            i+=1

        i = len(nums) - 2
        rev[-1] = nums[-1]
        while i >= 0 :
            rev[i] = rev[i+1] * nums[i]
            i-=1
        
        ret_arr = [0] * len(nums)
        ret_arr[0], ret_arr[-1] = rev[1], prod[-2]
        i = 1
        while i < len(nums) - 1 :
            ret_arr[i] = rev[i+1] * prod[i-1]
            i+=1
        return ret_arr