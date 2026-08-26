class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = defaultdict(int)

        for i in nums :
            d[i] += 1
        
        return sorted([i for i in d.keys()], key=lambda l: d[l], reverse=True)[:k]
