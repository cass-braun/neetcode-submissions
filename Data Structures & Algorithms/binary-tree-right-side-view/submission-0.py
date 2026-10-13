# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])        
        res = []

        while q:
            for _ in range(len(q)-1):
                curr = q.popleft()
                
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            visible = q.popleft()
            res.append(visible.val)

            if(visible.left):
                q.append(visible.left)
            if(visible.right):
                q.append(visible.right)
        
        return res