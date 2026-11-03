class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        heights = [0]*n # index = node, value = height


        adj = [[] for _ in range(n)] # index = node, value = [node list]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        minHeight = float('inf')
        for i, edges in enumerate(adj):
            inTree = [False]*n

            inTree[i] = True

            q = deque([edges])
            height = 0
            
            while q:
                level = q.pop()
                height +=1
                
                nextLevel = []
                for newE in level:
                    inTree[newE] = True
                    for newEdge in adj[newE]:
                        if not inTree[newEdge]:
                            nextLevel.append(newEdge)
                
                if len(nextLevel) != 0:
                    q.append(nextLevel)
            
            heights[i] = height
            minHeight = min(height, minHeight)
        
        res = []
        for i, h in enumerate(heights):
            if h == minHeight:
                res.append(i)
        return res

