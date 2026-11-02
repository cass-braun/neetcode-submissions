# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node, parent, side):
            if node is None:
                return

            dfs(node.left, node, 'l')
            dfs(node.right, node, 'r')
            

            if not node.right and not node.left and node.val == target:
                if side == 'l':
                    parent.left = None
                else:
                    parent.right = None

        dfs(root.left, root, 'l')
        dfs(root.right, root, 'r')

        if root.left is None and root.right is None and root.val == target:
            return None

        return root            