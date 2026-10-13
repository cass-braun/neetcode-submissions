# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(curr, depth):
            maxLeft = max(dfs(curr.left, depth+1) if curr.left else depth, depth)

            maxRight = max(dfs(curr.right, depth+1) if curr.right else depth, depth)

            return max(maxLeft, maxRight)

        return dfs(root, 1)
        