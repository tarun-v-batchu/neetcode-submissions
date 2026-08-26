class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t) :
            return False

        s_dic, t_dic = defaultdict(int), defaultdict(int)
        for i, j in zip(s, t) :
            s_dic[i] += 1
            t_dic[j] += 1
        
        for i in s_dic :
            if s_dic[i] != t_dic[i] :
                return False
        return True

