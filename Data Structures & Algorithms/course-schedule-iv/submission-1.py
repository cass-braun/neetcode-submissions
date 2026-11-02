class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)] # course = index, prereqs = item

        for p, c in prerequisites:
            adj[c].append(p)

        res = []
        for qP, qC in queries:
            q = deque([qC])
            visited = {qC}
            isPrereq = False
            
            while q and not isPrereq:
                course = q.pop()
                
                prereqs = adj[course]
                for prereq in prereqs:
                    if prereq == qP:
                        isPrereq = True
                        break
                    if prereq not in visited:
                        visited.add(prereq)
                        q.append(prereq)
            
            res.append(isPrereq)

        return res




