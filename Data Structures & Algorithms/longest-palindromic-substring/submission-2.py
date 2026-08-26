class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = s[0]
        for k in range(len(s)) :
            
            i = k
            j = k
            print("index:", i)
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            max_str = max(s[i + 1:j], max_str, key=lambda x: len(x))
            
            i = k
            j = k + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            max_str = max(s[i + 1:j], max_str, key=lambda x: len(x))
        
        return max_str
