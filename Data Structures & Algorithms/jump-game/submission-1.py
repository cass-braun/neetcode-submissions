class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        reachable = [False]*len(nums)

        reachable[len(nums)-1] = True
        for i in range(len(nums)-2, -1, -1):
            j = 1
            
            while j <= nums[i] and not reachable[i]:
                if i+j >=len(nums) or reachable[i+j]:
                    reachable[i] = True
            
                j +=1
        
        return reachable[0]