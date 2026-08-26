class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        dic = defaultdict(int)
        i,j = 0,0
        max_length = 0
        while j < len(s) :
            dic[s[j]] += 1
            if max(dic.values()) < (j - i + 1) - k :
                dic[s[i]] -= 1
                i += 1
            max_length = max(max_length, j - i + 1)
            j += 1

        return max_length


    
