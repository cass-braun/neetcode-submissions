import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxFreq = 0

        freqs = [0]*26
        
        for t in tasks:
            index = ord(t) - ord('A')
            freqs[index] -= 1

        h = []
        for f in freqs:
            if f != 0:
                h.append(f)

        heapq.heapify(h)

        time = 0
        q = deque()

        while h or q:
            time += 1

            if q and q[0][1] == time:
                freq, _ = q.popleft()
                heapq.heappush(h, freq)
            
            if h:
                freq = heapq.heappop(h)
                freq += 1

                if freq < 0:
                    q.append((freq, time + n+1))
            else:
                if q:
                    time = q[0][1] - 1
        return time