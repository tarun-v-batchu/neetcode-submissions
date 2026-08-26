class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0 :
            return 0

        mini = min(nums)
        maxi = max(nums)

        arr = [0] * (maxi - mini + 1)
        for i in nums :
            arr[i-mini]+=1
        
        print(arr)
        
        max_seq = -1
        curr_seq = 0
        for i in arr :
            # print(max_seq)
            if i == 0 :
                if max_seq < curr_seq :
                    max_seq = curr_seq
                curr_seq = 0
            else :
                # print(i, curr_seq)
                curr_seq += 1

        return max_seq if max_seq > curr_seq else curr_seq
            
            



