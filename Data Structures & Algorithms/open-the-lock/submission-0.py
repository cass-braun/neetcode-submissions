from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        
        if "0000" in dead_set:
            return -1
        
        if target == "0000":
            return 0
            
        queue = deque([("0000", 0)]) # stores (current_state, turns)
        visited = {"0000"}
        
        def get_neighbors(s):
            neighbors = []
            for i in range(4):
                digit = int(s[i])
                # Turn up
                neighbors.append(s[:i] + str((digit + 1) % 10) + s[i+1:])
                # Turn down
                neighbors.append(s[:i] + str((digit - 1) % 10) + s[i+1:])
            return neighbors

        while queue:
            curr_state, turns = queue.popleft()
            
            if curr_state == target:
                return turns
                
            for neighbor in get_neighbors(curr_state):
                if neighbor not in dead_set and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, turns + 1))
                    
        return -1