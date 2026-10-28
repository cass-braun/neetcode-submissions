class Solution:
    def tribonacci(self, n: int) -> int:
        prev = [0,1,1]

        if n == 0:
            return 0
        if n == 2 or n == 1:
            return 1

        res = 2
        for _ in range(3, n+1):
            curr = sum(prev)
            prev[0] = prev[1]
            prev[1] = prev[2]
            prev[2] = curr

        return prev[2]