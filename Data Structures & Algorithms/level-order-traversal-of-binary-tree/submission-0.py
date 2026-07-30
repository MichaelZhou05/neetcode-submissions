# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret = [[]]
        ret[-1].append(root.val)
        
        def loTravers(root, level) -> None :
            nonlocal ret

            if not root:
                return
            if level+2 > len(ret) :
                ret.append([])
            if root.left:
                ret[level+1].append(root.left.val)
            if root.right:
                ret[level+1].append(root.right.val)
            
            loTravers(root.left, level+1)
            loTravers(root.right, level+1)
        
        loTravers(root,0)
        return ret[0:-1]



        
        