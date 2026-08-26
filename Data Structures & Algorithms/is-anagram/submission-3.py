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
        # print(s_dic)
        # print(t_dic)
        
        for i in s_dic.keys() :
            if s_dic[i] != t_dic[i] :
                return False
        return True
