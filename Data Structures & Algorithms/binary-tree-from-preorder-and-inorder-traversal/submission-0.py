# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0], None, None)
        mid = inorder.index(preorder[0])
        preorder.pop(0)

        def helper(inorder) -> TreeNode: 
            nonlocal preorder

            if not preorder or not inorder :
                return None

            val = preorder.pop(0)
            node = TreeNode(val)
            
            
            mid = inorder.index(val)
            node.left = helper(inorder[0:mid])
            node.right = helper(inorder[mid+1:])
            return node
            

        root.left = helper(inorder[:mid]) 
        root.right = helper(inorder[mid+1:])

        return root

    

            











        # curr = root

        # i, j = 0
        # while not preorder[i] == inorder[0] :
        #     curr.left = preorder[i] if preorder[i] != root.val else None
        #     curr = curr.left 
        #     i += 1
        #curr must be at the left most Node


