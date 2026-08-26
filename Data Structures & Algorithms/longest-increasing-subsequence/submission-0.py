class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def recurse(i, nums, memo) :
            if i >= len(nums) :
                return 0
            if i in memo :
                return memo[i]

            j = i + 1
            recurse(i + 1, nums, memo)
            max_seq = 1
            while j < len(nums) :
                if nums[i] < nums[j] :
                    # print(i, j)
                    j_rec = recurse(j, nums, memo) + 1
                    # print(i, j, j_rec)
                    max_seq = max(max_seq, j_rec)
                j += 1
            
            memo[i] = max_seq
            # print(i, max_seq, memo)
            return max_seq

        memo = {}        
        recurse(0, nums, memo)
        # print(memo)
        return max([memo[i] for i in memo])
