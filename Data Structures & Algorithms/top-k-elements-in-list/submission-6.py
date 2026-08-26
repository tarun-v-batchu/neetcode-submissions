class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = defaultdict(int)
        for i in nums :
            dic[i] += 1
        
        return sorted(dic, key = lambda x: dic[x])[-k:]