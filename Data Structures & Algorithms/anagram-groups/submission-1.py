class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)
        
        for i in strs :
            sorted_i = str(sorted(i))
            if sorted_i not in dic :
                dic[sorted_i] = [i]
            else :
                dic[sorted_i] += [i]
        
        return [dic[i] for i in dic]




