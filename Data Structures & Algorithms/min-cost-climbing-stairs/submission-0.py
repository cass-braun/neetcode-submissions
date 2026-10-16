class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCostToReach = [0,0]

        for i in range(2, len(cost)+1):
            minCostLeft = cost[i-2] + minCostToReach[i-2]
            minCostRight = cost[i-1] + minCostToReach[i-1]
            minCostToReach.append(min(minCostLeft,minCostRight))

        return minCostToReach[-1]
