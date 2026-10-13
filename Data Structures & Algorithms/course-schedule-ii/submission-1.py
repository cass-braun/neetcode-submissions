class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        state = [0]*numCourses

        root = {}
        for course, prereq in prerequisites:
            if course not in root:
                root[course] = [prereq]
            else:
                root[course].append(prereq)


        output = []

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1

            if course in root:
                for p in root[course]:
                    if not dfs(p):
                        return False
            
            state[course] = 2
            output.append(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []

        return output

