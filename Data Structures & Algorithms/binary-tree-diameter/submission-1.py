# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dob(root) -> []:  #[height, maxDia]
            if not root:
                return [0,0]
            else:
                l = dob(root.left)
                r = dob(root.right)
                return [1 + max(l[0],r[0]), max(l[0]+r[0], max(l[1],r[1]))]
        
        ls1 = dob(root)
        return ls1[1]

    
    

