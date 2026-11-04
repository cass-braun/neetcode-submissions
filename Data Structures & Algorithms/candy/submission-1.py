class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        # Every child must get at least 1 candy (the local minimum baseline)
        candies = [1] * n
        
        # 1. Left-to-right pass: if current > previous, give more than previous
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        # 2. Right-to-left pass: if current > next, give more than next
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # Take the max to satisfy both left and right neighbor constraints
                candies[i] = max(candies[i], candies[i + 1] + 1)
                
        return sum(candies)