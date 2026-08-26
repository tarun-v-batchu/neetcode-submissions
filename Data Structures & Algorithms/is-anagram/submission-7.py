class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) :
            return False
        
        
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)

        for i in range(len(s)) :
            s_dic[s[i]] += 1
            t_dic[t[i]] += 1
        
        return s_dic == t_dic


