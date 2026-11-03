import math

class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize dp array with infinity, base case dp[0] = 0
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Precompute all possible square numbers <= n
        squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        
        # Build up the dp table from 1 to n
        for target in range(1, n + 1):
            for sq in squares:
                if target < sq:
                    break
                dp[target] = min(dp[target], dp[target - sq] + 1)
                
        return dp[n]