import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
    def findMedian(self) -> float:

        if(len(self.minHeap) == len(self.maxHeap)):
            return (self.minHeap[0] + -self.maxHeap[0])/2

        if(len(self.minHeap) > len(self.maxHeap)):
            return self.minHeap[0]

        
        return self.maxHeap[0]*-1