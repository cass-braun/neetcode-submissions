import math

class Solution:
    def numSquares(self, n: int) -> int:
        maxRoot = int(math.sqrt(n))

        dp= [0]*(n+1)


        for total in range(1,n+1):
            minNums = total
            
            for currRoot in range(1, maxRoot+1):
                if currRoot**2 > total:
                    continue

                minNums = min(minNums, dp[total - currRoot**2]+1)

            dp[total] = minNums

        return dp[n]    
