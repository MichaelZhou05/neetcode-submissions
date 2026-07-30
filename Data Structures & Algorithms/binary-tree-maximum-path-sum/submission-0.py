# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = float("-inf")


        def search(root) -> int :
            nonlocal maxVal

            if not root :
                return 0
            
            leftVal = search(root.left)
            rightVal = search(root.right)
            ret = max(rightVal + root.val, leftVal + root.val, root.val)
            maxVal = max(maxVal, ret, rightVal + leftVal + root.val)
            return ret
        
        val = search(root)

        return maxVal


            

            