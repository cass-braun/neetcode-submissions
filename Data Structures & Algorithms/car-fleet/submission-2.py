class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedArr = []
        for i in range(len(position)):
            p, v = position[i], speed[i]

            heapq.heappush(sortedArr, (-p, v) )

        stack = []
        while sortedArr:
            p, s = heapq.heappop(sortedArr)
            p *= -1
            time_to_target = (target - p) / s
            stack.append(time_to_target)
            
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        # The number of items left in the stack represents the total number of fleets
        return len(stack)
