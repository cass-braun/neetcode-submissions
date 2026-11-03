class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_reachable = [[False] * numCourses for _ in range(numCourses)]
        
        for u, v in prerequisites:
            is_reachable[u][v] = True
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_reachable[i][k] and is_reachable[k][j]:
                        is_reachable[i][j] = True
                        
        return [is_reachable[qP][qC] for qP, qC in queries]
