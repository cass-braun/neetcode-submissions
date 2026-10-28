class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for i in range(len(coins)+1)]
        dp[0][0] = 1

        res = 0

        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(1, len(coins)+1):
            coin = coins[i-1]
            
            for j in range(1, amount+1):
                without_coin = dp[i - 1][j]
                
                with_coin = dp[i][j - coin] if j >= coin else 0
                
                dp[i][j] = without_coin + with_coin
                

        
        return dp[-1][-1]
                
                

