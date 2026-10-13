from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                count +=1
                visited.add(i)
                q = deque([i])

                while q:
                    curr = q.popleft()

                    for n in adj[curr]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
        return count
