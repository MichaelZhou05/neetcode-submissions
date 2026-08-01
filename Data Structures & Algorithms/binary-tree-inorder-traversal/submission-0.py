# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

    
        def inOrder(node) -> List[int]:
            if node == None:
                return []
            
            left = inOrder(node.left)
            left.append(node.val)
            return left + inOrder(node.right)
        
        return inOrder(root)
    