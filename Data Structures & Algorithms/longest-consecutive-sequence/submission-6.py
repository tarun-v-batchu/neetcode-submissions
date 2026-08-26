class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0 :
            return 0
        
        mini = min(nums)
        maxi = max(nums)
        
        array = [False] * (maxi - mini + 1)

        for i in nums :
            # print(i, mini, maxi, i - mini)
            # print(len(array))
            array[i - mini] = True
        
        max_seg = 0
        
        i = 0
        # print(array)
        while i < len(array) :
            curr_seg = 0
            while i < len(array) and array[i] :
                curr_seg += 1
                i += 1
            max_seg = max(max_seg, curr_seg)
            # print(max_seg)
            i += 1

        return max_seg