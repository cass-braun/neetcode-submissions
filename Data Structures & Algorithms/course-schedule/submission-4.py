class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        root = {}
        for prereq, course in prerequisites:
            if course not in root:
                root[course] = [prereq]
            else:
                root[course].append(prereq)

        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1
            
            if course in root:
                for prereq in root[course]:
                    if not dfs(prereq):
                        return False
            
            state[course] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True