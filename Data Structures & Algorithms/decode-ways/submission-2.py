class Solution:
    def numDecodings(self, s: str) -> int :
    
        def valid_two_dig(i, j) :
            if i == 2 :
                return 1 if j <= 6 else 0
            return 1 if i == 1 else 0
        
        if s[0] == '0' :
            return 0
        if len(s) == 1 :
            return 1
        nums = [0] * len(s)
        nums[0] = 1
        nums[1] = (1 if s[1] != '0' else 0) + (1 if valid_two_dig(int(s[0]), int(s[1])) else 0)
        if nums[1] == 0 :
            return 0
        i = 2
        while i < len(s) :
            print(nums[i - 1], nums[i - 2])
            nums[i] = (nums[i - 1] if s[i] != '0' else 0) + (nums[i - 2] if valid_two_dig(int(s[i - 1]), int(s[i])) else 0)
            if nums[i] == 0 :
                return 0
            i += 1
            print(nums)
        return nums[-1]
