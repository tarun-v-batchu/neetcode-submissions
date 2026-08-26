import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        heapq.heapify(arr)

        for i in nums :
            heapq.heappush(arr, i)
            if len(arr) > k :
                heapq.heappop(arr)
        
        return min(arr)
