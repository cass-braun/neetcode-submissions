class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, cur, current_target):
            if current_target == 0:
                res.append(cur.copy())
                return
            
            if current_target < 0 or i >= len(nums):
                return
            
            for j in range(i, len(nums)):
                cur.append(nums[j])
                
                backtrack(j, cur, current_target - nums[j])
                
                cur.pop()

        backtrack(0, [], target)
        return res
