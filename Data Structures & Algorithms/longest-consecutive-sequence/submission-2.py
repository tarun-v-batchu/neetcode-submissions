class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not len(nums) :
            return 0

        mini = min(nums)
        maxi = max(nums)


        arr = [0] * (maxi - mini + 1)
        
        for i in nums :
            arr[i - mini]+=1

        # print(arr)

        segment = 0
        max_segment = 1
        i = 1
        while i <= len(arr) :
            if arr[i-1] :
                segment += 1
                # print(arr[i-1], segment)
            else:
                segment = 0
                # print("Restart", segment)
            if segment > max_segment:
                max_segment = segment
            i += 1

        return max_segment



