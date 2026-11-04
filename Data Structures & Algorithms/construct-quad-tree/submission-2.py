"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 0:
            return None
            
        # 1. Build a 2D Prefix Sum matrix for O(1) range sum queries
        # prefix[r][c] stores the sum of all elements from grid[0][0] to grid[r-1][c-1]
        prefix = [[0] * (n + 1) for _ in range(n + 1)]
        for r in range(n):
            for c in range(n):
                prefix[r + 1][c + 1] = grid[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
                
        def makeNode(sr, er, sc, ec):
            # Calculate the total sum of the sub-grid using the prefix sum matrix in O(1)
            total = prefix[er][ec] - prefix[sr][ec] - prefix[er][sc] + prefix[sr][sc]
            area = (er - sr) * (ec - sc)
            
            # If all cells are 0 or all cells are 1, it's a leaf node
            if total == 0:
                return Node(val=False, isLeaf=True)
            elif total == area:
                return Node(val=True, isLeaf=True)
            
            # Otherwise, it's a non-leaf node; split into 4 quadrants
            midR = sr + (er - sr) // 2
            midC = sc + (ec - sc) // 2
            
            topLeft = makeNode(sr, midR, sc, midC)
            topRight = makeNode(sr, midR, midC, ec)
            bottomLeft = makeNode(midR, er, sc, midC)
            bottomRight = makeNode(midR, er, midC, ec)
            
            return Node(val=True, isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)

        return makeNode(0, n, 0, n)
            