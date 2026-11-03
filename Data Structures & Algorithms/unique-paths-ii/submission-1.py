class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [ [0]*COLS for _ in range(ROWS)]

        target = [ ROWS - 1, COLS - 1]
        dp[ROWS - 1][COLS-1] = 1

        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        d = [(0, 1), (1, 0)]
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                numPaths = 0
                if r == ROWS-1 and c == COLS-1:
                    continue
                    

                for dr, dc in d:
                    nr, nc = r+dr, c+dc
                    if -1 < nr < ROWS and -1 < nc < COLS and obstacleGrid[nr][nc] == 0:
                        numPaths += dp[nr][nc]
                
                dp[r][c] = numPaths

        return dp[0][0]