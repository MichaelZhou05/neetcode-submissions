# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(root, maxVal, minVal) :
            if not root: 
                return True
            if root.val < maxVal and root.val > minVal :
                return bfs(root.left, min(maxVal, root.val), minVal) and bfs(root.right, maxVal, max(minVal, root.val))
            else:
                return False
            
        
        return bfs(root, float("inf"), float("-inf"))
            
            
            
            