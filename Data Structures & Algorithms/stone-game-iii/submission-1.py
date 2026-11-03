class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        ''' Options:
        1. take 1
        2. take 2
        3. take 3
        
        optimal when taking max future value of 1,2, or 3
        '''

        maxDiff = [ 0 ]*(len(stoneValue)+3)

        for i in range(len(stoneValue)-1, -1, -1 ):
            take1 = stoneValue[i] - maxDiff[i+1]
            take2 = stoneValue[i] + stoneValue[i+1] - maxDiff[i+2] if i+1 < len(stoneValue) else -float('inf')
            take3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - maxDiff[i+3] if i+2 < len(stoneValue) else -float('inf')

            maxDiff[i] = max(take1, take2, take3)
        
        return 'Alice' if maxDiff[0] > 0 else 'Bob' if maxDiff[0]<0 else 'Tie'


