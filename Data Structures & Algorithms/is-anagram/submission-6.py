class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)

        for i in s :
            s_dic[i] += 1
        for i in t :
            t_dic[i] += 1
        
        return [(i,  s_dic[i]) for i in sorted(s_dic)] == [(i,  t_dic[i]) for i in sorted(t_dic)]


