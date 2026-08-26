class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            print("hi")
            return False
        
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)


        for i in s :
            s_dic[i] += 1
        
        for j in t :
            t_dic[j] += 1

        # print("s")
        # for i in s:
        #     print(i, s_dic[i])
        # print("t")
        # for i in t :
        #     print(i, t_dic[i])
        
        for i in s :
            if t_dic[i] != s_dic[i] :
                return False
        return True
        
