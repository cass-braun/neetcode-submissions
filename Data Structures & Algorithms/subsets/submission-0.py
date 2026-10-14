class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        empty = ()
        subsets.append(empty)

        for n in nums:
            for s in subsets:
                if n not in s:
                    newS = s + (n,)
                    subsets.append(newS)
                
        newSets = []

        for s in subsets:
            newSets.append(list(s))
        
        return newSets