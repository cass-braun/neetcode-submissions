class Solution:
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        totalGas = 0
        totalCost = 0
        
        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
    
        if totalGas < totalCost:
            return -1

        
        total = 0
        index = 0

        for i in range(len(gas)):
            total += gas[i]
            total -= cost[i]
            
            if(total < 0):
                total = 0
                index = i + 1
        return index