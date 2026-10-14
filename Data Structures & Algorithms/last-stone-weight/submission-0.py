import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        elif len(stones ) == 0:
            return 0

        heap = []
        for stone in stones:
            heap.append(stone*-1)

        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x != y:
                remaining = x - y 
                heapq.heappush(heap, remaining)

        
        if len(heap) == 1:
            return -1*heapq.heappop(heap)
        return 0