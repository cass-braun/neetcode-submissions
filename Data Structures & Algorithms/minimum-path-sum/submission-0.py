class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        dp = [ [0]*COLS for _ in range(ROWS) ]

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                rightCost = dp[r][c+1] if -1 < c+1 < COLS else 0

                downCost = dp[r+1][c] if -1 < r+1 < ROWS else 0

                dp[r][c] = grid[r][c]
                if rightCost != 0 and downCost != 0:
                    dp[r][c] += min(rightCost, downCost)
                elif rightCost != 0 or downCost != 0:
                    dp[r][c] += max(rightCost, downCost)
                
                print(r, ' ', c, ' ', grid[r][c])

        
        print(dp)
        return dp[0][0]





