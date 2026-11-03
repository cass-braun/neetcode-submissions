class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numPrereqs = {}
        prereqs = {}

        for i in range(numCourses):
            numPrereqs[i] = 0
            prereqs[i] = []
        
        for p, c in prerequisites:
            numPrereqs[c] += 1
            
            prereqs[p].append(c)

        q = deque()
        
        for key, value in numPrereqs.items():
            if value == 0:
                q.append(key)
        
        while q:
            prereq = q.popleft()
            courses = prereqs[prereq]

            for course in courses:
                if numPrereqs[course] > 0:
                    numPrereqs[course] -= 1
                if numPrereqs[course] == 0:
                    q.append(course)

        for value in numPrereqs.values():
            if value != 0:
                return False
        
        return True


            