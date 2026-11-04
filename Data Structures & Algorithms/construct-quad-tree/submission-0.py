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
        if len(grid) == 0:
            return None
        def makeNode(sr, er, sc, ec):
            val = grid[sr][sc]
            isLeaf = True
            for r in range(sr, er):
                for c in range(sc, ec):
                    if grid[r][c] != val:
                        isLeaf = False
                        break
            
            if not isLeaf:
                midR = sr + (er-sr)//2
                midC = sc + (ec-sc)//2

                topLeft = makeNode(sr, midR, sc, midC)
                topRight = makeNode(sr, midR, midC, ec)
                bottomLeft = makeNode(midR, er, sc, midC)
                bottomRight = makeNode(midR, er, midC, ec)

                return Node(val, False, topLeft, topRight, bottomLeft, bottomRight)



            return Node(val, True)

        return makeNode(0, len(grid), 0, len(grid[0]))
            