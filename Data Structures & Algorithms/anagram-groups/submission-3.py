class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for s in strs :
            dic[str(sorted(s))] += [s]
        
        return [dic[i] for i in dic]

        
