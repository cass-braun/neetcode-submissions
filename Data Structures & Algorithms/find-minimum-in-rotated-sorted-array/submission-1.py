class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        if len(nums) == 1:
            return minVal

        def bs(start, end):
            mid = (start+end)//2
            print(nums[start:end+1])
            if -1 <= start-end <= 1:
                if nums[start] < minVal:
                    return start
                else: return end
            if nums[mid] > minVal:
                #search higher
                return bs(mid, end)
            if nums[mid] < minVal:
                return bs(start, mid)

        
        newMinIndex = bs(1, len(nums)-1)

        return min(minVal, nums[newMinIndex])