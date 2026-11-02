class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {} # value, index in array


        for index, num  in enumerate(nums):
            if target-num not in values:
                values[num] = index
            else:
                return [ values[target-num], index ]
        
        return []