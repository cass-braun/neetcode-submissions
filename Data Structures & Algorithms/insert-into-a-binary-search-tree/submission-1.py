# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        def insert(curr):

            if curr.val > val:
                if curr.left is not None:
                    insert(curr.left)
                else:
                    curr.left = TreeNode(val)
            
            if curr.val < val:
                if curr.right is not None:
                    insert(curr.right)
                else:
                    curr.right = TreeNode(val)

        insert(root)
        return root