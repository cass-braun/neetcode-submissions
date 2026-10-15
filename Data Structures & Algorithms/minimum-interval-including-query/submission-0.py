class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])

        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])


        res = {}
        min_heap = []
        i = 0
        n = len(intervals)

        for q, original_index in sorted_queries:
            while i < n and intervals[i][0] <= q:
                start, end = intervals[i]
                length = end - start + 1

                heapq.heappush(min_heap, (length, end))
                i +=1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                res[original_index] = min_heap[0][0]
            else:
                res[original_index] = -1
        
        return [res[idx] for idx in range(len(queries))]