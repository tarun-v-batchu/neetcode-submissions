class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for i in strs :
            sorted_word = sorted(i)
            dic["".join(sorted_word)] += [i]
        return [dic[i] for i in dic]



