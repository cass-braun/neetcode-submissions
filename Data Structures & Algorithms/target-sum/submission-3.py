class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Target must be within [-total_sum, total_sum]
        if not (-total_sum <= target <= total_sum):
            return 0

        # Size of DP table is 2 * total_sum + 1 to accommodate negative sums
        offset = total_sum
        dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums) + 1)]
        
        # Base case: 0 ways to get any sum initially, except sum 0 at the offset index
        dp[0][offset] = 1
        
        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            for j in range(len(dp[0])):
                # Check if previous state (j - num) is within bounds
                added = dp[i - 1][j - num] if 0 <= j - num < len(dp[0]) else 0
                
                # Check if previous state (j + num) is within bounds
                subtracted = dp[i - 1][j + num] if 0 <= j + num < len(dp[0]) else 0
                
                dp[i][j] = added + subtracted
                
        # Return the result at target shifted by the offset
        return dp[len(nums)][target + offset]