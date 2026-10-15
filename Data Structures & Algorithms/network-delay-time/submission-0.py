import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        paths = { i: [] for i in range(1, n + 1)}
        for u, v, t in times:
            paths[u].append((v, t))
            
        minTimes = {i: float("inf") for i in range(1, n + 1)}
        minTimes[k] = 0
        
        priority_queue = [(0, k)]
        
        while priority_queue:
            currTime, node = heapq.heappop(priority_queue)
            
            if currTime > minTimes[node]:
                continue
                
            for dest, time in paths[node]:
                if currTime + time < minTimes[dest]:
                    minTimes[dest] = currTime + time
                    heapq.heappush(priority_queue, (currTime + time, dest))
                    
        maxVal = max(minTimes.values())
        
        return maxVal if maxVal != float('inf') else -1
        

