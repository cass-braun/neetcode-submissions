class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trieDict = {}

        for word in dictionary:
            curr = trieDict
            for char in word:
                if char not in curr:
                    curr[char] = {}
                
                curr = curr[char]
            
            curr['*'] = True
        
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            # Option 1: Treat s[i] as an extra character
            dp[i] = 1 + dp[i + 1]
            
            # Option 2: Check if any dictionary word starts at index i using the Trie
            curr = trieDict
            for j in range(i, n):
                if s[j] not in curr:
                    break
                curr = curr[s[j]]
                if '*' in curr:
                    # If a valid word exists from i to j, transition to dp[j + 1]
                    dp[i] = min(dp[i], dp[j + 1])
                    
        return dp[0]



