class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t) :
            return False
        
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)
        for i in s :
            s_dic[i] += 1
        for i in t :
            t_dic[i] += 1
        
        for key in s_dic :
            if s_dic[key] != t_dic[key] :
                return False
        return True
        

