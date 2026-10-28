class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i1 in range(m - 1, -1, -1):
            for i2 in range(n - 1, -1, -1):
                if text1[i1] == text2[i2]:
                    dp[i1][i2] = 1 + dp[i1 + 1][i2 + 1]
                else:
                    dp[i1][i2] = max(dp[i1 + 1][i2], dp[i1][i2 + 1])
        
        return dp[0][0]




        
        