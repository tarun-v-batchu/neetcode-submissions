class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        m = defaultdict(list)
        for word in strs :
            m[str(sorted(word))] += [word]
        
        return [m[i] for i in m] 
