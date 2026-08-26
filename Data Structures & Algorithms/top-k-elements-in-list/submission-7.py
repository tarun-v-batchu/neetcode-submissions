import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        heap = []
        for i in c :
            if len(heap) < k :
                heapq.heappush(heap, (c[i], i))
            else :
                heapq.heappushpop(heap, (c[i], i))
        
        return sorted([i for _,i in heap])
