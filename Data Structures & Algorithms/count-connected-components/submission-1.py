from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])  # Path compression
            return parent[i]

        components = n
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            
            if root_u != root_v:
                parent[root_u] = root_v
                components -= 1

        return components
