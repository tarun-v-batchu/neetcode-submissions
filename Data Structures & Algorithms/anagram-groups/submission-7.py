class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs :
            dic["".join(sorted(i))].append(i)
        
        return [dic[i] for i in dic]