# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(root) -> int :
            if not root :
                return 0 
            
            l = height(root.left)
            r = height(root.right)
            h = 1 + max(l, r) if abs(l - r) < 2 else float('-inf')
            return h

        count = height(root)
        return True if count > 0 else False
        

