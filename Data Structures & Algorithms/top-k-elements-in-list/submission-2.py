class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        a = defaultdict(int)

        for i in nums :
            a[i] += 1
        return sorted(a, reverse=True, key=lambda x: a[x])[:k]