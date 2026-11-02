class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
            
        max_len = 1
        l = 0
        
        def getSign(i, j):
            if arr[i] < arr[j]:
                return 1
            elif arr[i] > arr[j]:
                return -1
            else:
                return 0

        for r in range(1, n):
            curr_sign = getSign(r - 1, r)
            
            if curr_sign == 0:
                # Two adjacent elements are equal -> streak resets
                l = r
            elif r == n - 1 or curr_sign * getSign(r, r + 1) != -1:
                # The alternation breaks (or we hit the end of the array)
                max_len = max(max_len, r - l + 1)
                l = r  # Start a new window from the current element
                
        return max_len