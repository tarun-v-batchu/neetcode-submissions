class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        arr = []
        
        max_string = 0
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            while j < len(s) and s[j] not in arr :
                arr.append(s[j])
                j+=1
            if j - i > max_string :
                print(i, j, j - i)
                max_string = j - i
            if j >= len(s) :
                return max_string
            while i < len(s) and s[j] in arr :
                arr.remove(s[i])
                i+=1
            arr.append(s[j])
            j+=1
        return max_string
