class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        memo = {} # Stores the longest increasing path starting at (r, c)
        
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
                
            ans = 1 # Minimum path length is 1 (the cell itself)
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # Check bounds and ensure the path is strictly increasing
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    ans = max(ans, 1 + dfs(nr, nc))
                    
            memo[(r, c)] = ans
            
            return ans
            
        max_path = 0
        for r in range(rows):
            for c in range(cols):
                max_path = max(max_path, dfs(r, c))
                
        return max_path
