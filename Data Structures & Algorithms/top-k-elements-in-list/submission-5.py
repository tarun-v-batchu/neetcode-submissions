class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = defaultdict(int)
        for i in nums :
            dic[i] += 1
        arr = sorted([(index, dic[index]) for index in dic], key=lambda x: x[1])[-k:]
        
        return [a[0] for a in arr]