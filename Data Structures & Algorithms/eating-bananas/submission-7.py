class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Koko's speed must be at least 1, never 0
        minK = 1
        maxK = max(piles)
        
        def canEatBananas(k):
            hoursTaken = 0
            for p in piles:
                hoursTaken += p // k
                if p % k != 0:
                    hoursTaken += 1
            return hoursTaken <= h

        def bs(left, right):
            if left > right:
                return left
            
            mid = (left + right) // 2
            
            if canEatBananas(mid):
                # Speed works, try to find a smaller valid speed on the left
                return bs(left, mid - 1)
            else:
                # Too slow, increase speed on the right
                return bs(mid + 1, right)
        
        return bs(minK, maxK)