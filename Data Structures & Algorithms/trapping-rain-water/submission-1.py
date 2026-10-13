class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1 or len(height) == 2:
            return 0
        
        prefixMax = [0]*len(height)
        suffixMax = [0]*len(height)

        iMax = 0
        
        for i in range(1, len(height)-1):
            iMax = max(iMax, height[i-1])
            prefixMax[i] = iMax
        
        iMax = 0
        for i in range(len(height)-2, -1, -1):
            iMax = max(iMax, height[i+1])
            suffixMax[i] = iMax
    
        total = 0

        for i in range(1,len(height)-1):
            val =  min([prefixMax[i], suffixMax[i]]) - height[i]
            if (val >0):
                total += val
        return total
