class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0

        for n in nums:
            total +=n
        
        if total % 2 != 0:
            return False
        
        dp = [False] * (total//2 + 1)
        dp[0] = True 

        for n in nums:
            for i in range(total//2, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]

        return dp[total//2]