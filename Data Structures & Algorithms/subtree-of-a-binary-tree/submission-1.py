# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot: 
            return False

        def comp(l, r) :
            if not l and not r :
                return True
            if not l or not r :
                return False 
            if r.val != l.val :
                return False
            return comp(l.left, r.left) and comp(l.right, r.right)

        if root.val == subRoot.val :
            if comp(root, subRoot) :
                return True
            
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
