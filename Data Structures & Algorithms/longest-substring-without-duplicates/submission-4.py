class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        table = set()

        i = 0
        j = 0
        max_len = 0
        while j < len(s) :
            
            while j < len(s) and s[j] not in table :
                table.add(s[j])
                j += 1
            
            max_len = max(max_len, j - i)
            if j == len(s) :
                break
            
            while i < j and s[i] != s[j] :
                table.remove(s[i])
                i += 1
            table.remove(s[i])
            i += 1
            
        return max_len
            

