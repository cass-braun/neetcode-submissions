import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        
        for n in nums:
            heapq.heappush(heap, -1*n)

        for _ in range(k-1):
            heapq.heappop(heap)


        return heapq.heappop(heap)*-1