class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        numPrereqs = {}
        prereqs = {}

        for i in range(numCourses):
            numPrereqs[i] = 0
            prereqs[i] = []
        
        for c, p in prerequisites:
            prereqs[p].append(c)
            numPrereqs[c] += 1

        q = deque()
        for i in range(numCourses):
            if numPrereqs[i] == 0:
                q.append(i)
                
        res = []
        
        while q:
            p = q.popleft()
            res.append(p)
            
            for c in prereqs[p]:
                numPrereqs[c] -= 1
                if numPrereqs[c] == 0:
                    q.append(c)
                    
        return res if len(res) == numCourses else []

