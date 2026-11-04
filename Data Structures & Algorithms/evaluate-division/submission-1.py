class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        myDict = {}

        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]

            if not a in myDict: myDict[a] = {}
            myDict[a][b] = v

            if not b in myDict: myDict[b] = {}
            myDict[b][a] = 1/v


        def dfs(a, b, visited):
            if a not in myDict or b not in myDict:
                return -1
            if b in myDict[a]:
                return myDict[a][b]
            
            for c, newVal in myDict[a].items():
                if c not in visited:
                    visited.add(c)
                    res = dfs(c, b, visited)
                    if res != -1:
                        return res*newVal
                    visited.remove(c)
            return -1
        ans = []
        for c, d in queries:
            ans.append(dfs(c, d, set()))
        
        return ans
            

