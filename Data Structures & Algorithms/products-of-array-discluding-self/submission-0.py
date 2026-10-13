class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        cur = 1
        for i in range(1, len(nums)):
            cur *= nums[i-1]
            prefix[i] = cur
        
        cur = 1

        for i in range(len(nums)-2, -1, -1):
            cur *= nums[i+1]
            suffix[i] = cur
        
        res = []
        for x in range(0, len(nums)):
            res.append(prefix[x]*suffix[x])

        return res
            