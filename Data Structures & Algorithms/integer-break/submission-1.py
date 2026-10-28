class Solution:
    def integerBreak(self, n: int) -> int:
        maxProduct = [0]*(n+1)
        maxProduct[1] = 1

        for n1 in range(2, n+1):
            currMax = 0

            for i in range(1, n1):
                n11 = i
                n12 = n1-i
                newMax = max(n11, maxProduct[n11])*max(n12, maxProduct[n12])
                currMax = max(currMax, newMax)
            
            maxProduct[n1] = currMax
        return maxProduct[n]


