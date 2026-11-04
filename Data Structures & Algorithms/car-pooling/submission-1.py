class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxDist = -float('inf')
        for numP, f, t in trips:
            maxDist = max(maxDist, t)
        
        dp = [0]*maxDist

        for p, f, t in trips:
            for i in range(f, t):    
                dp[i] += p
                if dp[i] > capacity: return False
        
        return True