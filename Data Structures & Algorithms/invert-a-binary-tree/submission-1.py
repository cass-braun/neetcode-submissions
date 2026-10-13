# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def dfs(curr):

            if(curr.right and (curr.right.right or curr.right.left)):
                dfs(curr.right)
            if(curr.left and (curr.left.right or curr.left.left)):
                dfs(curr.left)
            
            temp = curr.right
            curr.right = curr.left
            curr.left = temp

        dfs(root)

        return root
