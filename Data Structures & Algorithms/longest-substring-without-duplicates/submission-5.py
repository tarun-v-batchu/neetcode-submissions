class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = set()

        i = 0
        j = 0
        max_length = 0

        while j < len(s) :
            while j < len(s) and s[j] not in d :
                d.add(s[j])
                j += 1
            max_length = max(max_length, j - i)
            if j >= len(s) :
                break
            
            while s[j] in d and i < j:
                d.remove(s[i])
                i += 1
        
        return max_length

