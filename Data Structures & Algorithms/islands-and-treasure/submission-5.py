class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        treasures = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasures.append([r,c])


        q = deque(treasures)

        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in d:
                nr, nc = r+dr, c+dc

                if -1 < nr < ROWS and -1 < nc < COLS and grid[r][c] + 1 < grid[nr][nc] and grid[nr][nc] != -1:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append([nr, nc])
        

        