# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(curr):
            if p.val > curr.val and q.val > curr.val:
                return lca(curr.right)
            if p.val < curr.val and q.val < curr.val:
                return lca(curr.left)

            else:
                return curr
        return lca(root)