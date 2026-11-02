class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_length = sum(nums)

        if total_length % k != 0:
            return False
        target = total_length//k
        
        if max(nums) > target:
            return False

        nums.sort()
        nums.reverse()

        sets = [0]*k
        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if sets[j] + nums[i] <= target:
                    sets[j] += nums[i]

                    if dfs(i+1):
                        return True
                    sets[j] -= nums[i]

                if sets[j] == 0:
                    break
            
            return False
        return dfs(0)


