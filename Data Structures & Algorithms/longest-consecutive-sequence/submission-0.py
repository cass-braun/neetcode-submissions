class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nDict = {}

        for n in nums:
            nDict[n] = False

        for n in nums:
            if n-1 not in nDict:
                nDict[n] = True
        
        longestSequence = 0

        for n, isStart in nDict.items():
            workingN = n
            currSequence = 1
            while isStart and workingN+1 in nDict:
                workingN+=1
                currSequence +=1
                
            longestSequence = max(longestSequence, currSequence)
    
        return longestSequence