# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bfs(root) :
            if not root: 
                return True
        
            l = root.left
            r = root.right
            if l :
                if l.val >= root.val: 
                    return False
                if l.right and l.right.val >= root.val :
                    return False
            if r  :
                if r.val <= root.val :
                    return False
                if r.left and r.left.val <= root.val :
                    return False
            
            return bfs(root.left) and bfs(root.right)
        
        return bfs(root)

            