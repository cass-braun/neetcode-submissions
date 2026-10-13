class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasVal = {}

        for n in nums:
            if n in hasVal:
                return True
            else:
                hasVal[n] = True

        return False
            
        