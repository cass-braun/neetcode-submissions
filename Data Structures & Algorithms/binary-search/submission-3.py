class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(startI, midI, endI):
            if nums[midI] == target:
                return midI

            if startI == endI:
                return -1
            if endI-startI == 1 or endI-startI == -1:
                if nums[endI] == target:
                    return endI
                if nums[startI] == target:
                    return startI
                return -1
            
            if nums[midI] > target:
                newMid =( midI+startI)//2
                return bs(startI, newMid, midI)
            else:
                newMid = (endI+midI)//2
                return bs(midI, newMid, endI)
            
        return bs(0, (len(nums)-1)//2, len(nums)-1)