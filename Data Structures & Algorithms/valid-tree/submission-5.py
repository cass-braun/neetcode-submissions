from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = []
        for i in range(n):
            parent.append(i)
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]


        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return False  
            parent[root_i] = root_j
            return True
        
        for u,v in edges:
            if not union(u,v):
                return False
        return True

