# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(pnode, qnode):
            if not pnode and not qnode:
                return True
            if not qnode or not pnode:
                return False
            if pnode.val != qnode.val:
                return False

            leftSame = dfs(pnode.left, qnode.left)
            rightSame = dfs(pnode.right, qnode.right)
            return leftSame and rightSame

        return dfs(p, q)