class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pq = []
        for i, (e, p) in enumerate(tasks):
            heapq.heappush(pq, (e, p, i))

        ans = []
        time = 0
        inqueue = []
        
        while pq or inqueue:
            # 1. Push all tasks that have arrived by 'time' into the available queue
            while pq and pq[0][0] <= time:
                e, p, i = heapq.heappop(pq)
                # Store as (processing_time, index) so the heap sorts by shortest job first, then smallest index
                heapq.heappush(inqueue, (p, i))
            
            if inqueue:
                # 2. Process the best available task
                p, i = heapq.heappop(inqueue)
                time += p
                ans.append(i)
            else:
                # 3. If CPU is idle, jump time forward to the next task's arrival time
                time = pq[0][0]
                
        return ans
