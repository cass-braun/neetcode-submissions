# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, maxTree):
            if not curr:
                return 0
            
            count = 1 if curr.val >= maxTree else 0

            new_max = max(maxTree, curr.val)

            return dfs(curr.left, new_max) + dfs(curr.right, new_max) + count

        return dfs(root, root.val)