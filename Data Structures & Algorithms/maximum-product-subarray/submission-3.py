class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            temp_max = max(n, curr_max * n, curr_min * n)
            curr_min = min(n, curr_max*n, curr_min*n)
            curr_max = temp_max

            res = max(res, curr_max)
        
        return res