class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        
        curr_max = 0
        max_sum = nums[0]
        
        curr_min = 0
        min_sum = nums[0]
        
        for n in nums:
            # 1. Standard Kadane's for Maximum Subarray Sum
            curr_max = max(curr_max + n, n)
            max_sum = max(max_sum, curr_max)
            
            # 2. Modified Kadane's for Minimum Subarray Sum
            curr_min = min(curr_min + n, n)
            min_sum = min(min_sum, curr_min)
            
            total_sum += n
        
        # If all numbers are negative, max_sum will be negative. 
        # In this case, total_sum - min_sum would be 0, which is wrong. 
        # We must return max_sum instead.
        if max_sum < 0:
            return max_sum
            
        # Return the maximum between the non-circular case and the circular case
        return max(max_sum, total_sum - min_sum)