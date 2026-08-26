class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for s in strs :    
            arr = "".join(sorted(s))
            d[arr] += [s]

        return [d[l] for l in d.keys()]
            
