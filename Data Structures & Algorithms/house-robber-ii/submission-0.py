class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob2(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            
            robValue = [nums[0], max(nums[0], nums[1])]

            for i in range(2, len(nums)):
                robValue.append(max(robValue[i-1], robValue[i-2]+nums[i]))
            return robValue[-1]
        
        if len(nums) ==1:
            return nums[0]
        return max( rob2(nums[1:]), rob2(nums[:len(nums)-1]))