# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:   
        def encode(node):
            if not node: 
                return 'N#'
            
            leftNode = encode(node.left)
            rightNode = encode(node.right)
            

            return str(node.val) + '#' + leftNode + rightNode 
        
        if not root:
            return ''
        return encode(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':
            return None

        vals = data.split('#')
        self.i = 0

        def construct():
            
            if self.i >= len(vals) or vals[self.i] == 'N' or vals[self.i] == '':
                self.i += 1
                return None



            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = construct()
            node.right = construct()
            

            return node
        
        return construct()



















            
            