class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        def getSubsets(i, comb):
            res.append(comb.copy())

            for j in range(i, len(nums)):
                if j == i or nums[j] != nums[j-1]:
                    comb.append(nums[j])

                    getSubsets(j+1, comb)

                    comb.pop()
        
        getSubsets(0, [])
        return res
                    
                    

