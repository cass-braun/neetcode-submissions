class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(conditions):
            # Adjacency list and in-degree array (1-indexed for convenience)
            adj = [[] for _ in range(k + 1)] # all items at index i appear below/right of i
            in_degree = [0] * (k + 1) # value at index indicates number of nodes above/left of i
            
            for u, v in conditions:
                adj[u].append(v)
                in_degree[v] += 1
                
            # Queue for nodes with 0 in-degree
            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            order = []
            
            while queue:
                curr = queue.popleft()
                order.append(curr)
                for neighbor in adj[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
                        
            # If we couldn't include all elements, there's a cycle
            if len(order) != k:
                return []
            return order

        # Get valid row and column orderings
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        
        # If either has a cycle, return an empty matrix
        if not row_order or not col_order:
            return []
            
        # Map each number to its row and column index
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        # Construct the matrix
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r = row_pos[num]
            c = col_pos[num]
            matrix[r][c] = num
            
        return matrix