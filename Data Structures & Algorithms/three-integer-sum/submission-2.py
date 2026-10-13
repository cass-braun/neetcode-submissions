class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  

        i = 0
        
        

        results = []
        
        while i < len(nums)-2:
            if i > 0 and nums[i] == nums[i - 1]:
                i+= 1
                continue

            j = i + 1
            k = len(nums)-1
            target = -nums[i]
            
            while j < k:
                currentSum = nums[j] + nums[k]
                if currentSum == target:
                    results.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j+= 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j+=1
                    k-=1
                elif currentSum > target:
                    k -= 1
                elif currentSum < target:
                    j += 1
                    
                


            i+= 1


        return results


        