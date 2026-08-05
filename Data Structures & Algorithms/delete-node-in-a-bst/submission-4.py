# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        parent = None
        def findNode(node,key):
            nonlocal parent
            if node == None:
                return

            if node.val == key:
                return node
            
            parent = node
    
            if key < node.val:
                return findNode(node.left,key)
            else:
                return findNode(node.right,key)
        
        deleteNode = findNode(root,key)

        if not deleteNode:
            return root

        replacement = deleteNode.right
        smallerNodes = deleteNode.left

        smallest = replacement
        while smallest.left:
            smallest = smallest.left
        
        smallest.left =smallerNodes

        if parent:
            if parent.left and parent.left.val == key :
                parent.left = replacement
            else:
                parent.right = replacement
        
        return root



            