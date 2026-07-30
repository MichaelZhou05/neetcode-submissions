# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root :
            return -1

        def height(root) :
            if not root:
                return 0
            else:
                return 1 +  max(height(root.left),height(root.right))

    
        length = height(root.left) + height(root.right)

        return max(length, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))
        
    


