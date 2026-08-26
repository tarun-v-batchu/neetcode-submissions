class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        for i in range(len(s)) :

            k = i
            j = i
            while k >= 0 and j < len(s) and s[k] == s[j] :
                count += 1
                k -= 1
                j += 1

            k = i
            j = i + 1
            while k >= 0 and j < len(s) and s[k] == s[j] :
                count += 1
                k -= 1
                j += 1

        
        return count
             