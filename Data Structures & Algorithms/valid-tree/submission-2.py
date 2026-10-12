from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges) != n-1):
            return False

        adj = [[] for _ in range(n)]

        for [s, e] in edges:
            if adj[s] == 0:
                adj[s] = [e]
            else:
                adj[s].append(e)

            if adj[e] == 0:
                adj[e] = [s]
            else:
                adj[e].append(s)

        visited = {0}


        q = deque( [(-1, 0)] )

        while q:
            parent, curr = q.popleft()
            
            
            for neighbour in adj[curr]:
                if neighbour in visited and neighbour != parent:
                    return False
                if neighbour != parent:

                    visited.add(neighbour)
                    q.append([curr, neighbour])
    
        return len(visited) == n





