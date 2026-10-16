import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        min_heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while min_heap:
            curr_time, r, c = heapq.heappop(min_heap)

            if r == n-1 and c == n-1:
                return curr_time

            for dr, dc in d:
                nr, nc = r+dr, c+dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr,nc))

                    next_time = max(curr_time, grid[nr][nc])

                    heapq.heappush(min_heap, (next_time, nr, nc))

    