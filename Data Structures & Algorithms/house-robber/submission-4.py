class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [ 0 ]*(len(nums)+2)

        for i in range(len(nums)):
            robHouse =  nums[i] + ( dp[i-2] if i-2 > -1 else 0)

            noRobHouse = dp[i-1] if i-1 > -1 else nums[i] 

            dp[i] = max(robHouse, noRobHouse)

        print(dp)
        return dp[len(nums)-1]
