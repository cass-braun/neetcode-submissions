class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mymap = {}

        for i,v in enumerate(nums):
            diff = target-v
            if target-v not in mymap:
                mymap[v] = i
            else: 
                if mymap[diff] < i:
                    return [mymap[diff], i]
                else:
                    return [i, mymap[diff]]
