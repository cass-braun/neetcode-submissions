class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courses = [ [] for _ in range(numCourses) ] # index = course, elements = prereq.s

        for p, c in prerequisites:
            courses[c].append(p)

        def dfs(course, target, visited):
            if course == target:
                return True
            visited.add(course)
            
            for nC in courses[course]:
                if nC not in visited and dfs(nC, target, visited):
                    return True
            
            return False


        answer = []
        
        for qP, qC in queries:
            answer.append(dfs(qC, qP, set() ))
        return answer

