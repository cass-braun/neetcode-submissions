class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Optional: Sort coins so the 'break' optimization is safe to use
        coins.sort()
        
        for target in range(1, amount + 1):
            for coin in coins:
                if target < coin:
                    break  # Safe now because coins are sorted
                
                dp[target] = min(dp[target], dp[target - coin] + 1)
        
        # 2. If dp[amount] is still infinity, it's impossible to form the amount -> return -1
        return dp[amount] if dp[amount] != float('inf') else -1