class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            
            if root_u == root_v:
                return False
            
            parent[root_u] = root_v
            return True
        
        for u, v in edges:
            if not union(u,v):
                return [u,v]
                
        