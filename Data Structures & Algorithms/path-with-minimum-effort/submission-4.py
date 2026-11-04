class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        d = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
        
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        efforts = { 0: { 0: 0 } }
        while pq:
            effort, r, c = heapq.heappop(pq)
            
            if r == ROWS -1 and c == COLS -1:
                return effort

            if r not in efforts: efforts[r] = {}
            

            for dr, dc in d:
                nr, nc = r+dr, c+dc

                if -1 < nr < ROWS and -1 < nc < COLS:
                    newEffort = max(effort, abs(heights[r][c] - heights[nr][nc]))

                    if nr in efforts and nc in efforts[nr]:
                        if newEffort < efforts[nr][nc]:
                            if nr not in efforts: efforts[nr] = {}
                            efforts[nr][nc] = newEffort
                            heapq.heappush(pq, (newEffort, nr, nc))
                    else:
                        if nr not in efforts: efforts[nr] = {}
                        efforts[nr][nc] = newEffort
                        heapq.heappush(pq, (newEffort, nr, nc))




