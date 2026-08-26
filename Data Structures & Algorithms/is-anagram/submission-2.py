class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t) :
            return False
        
        sd = defaultdict(int)
        td = defaultdict(int)
        
        i = 0
        while i < len(s) :
            sd[s[i]] += 1
            td[t[i]] += 1
            i += 1
        
        for j in s :
            if sd[j] != td[j] :
                return False
        return True
