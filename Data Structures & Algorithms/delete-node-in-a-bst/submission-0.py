# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def findNode(node,key):
            if node.left.val == key or node.right.val == key:
                return node
    
            if key < node.val:
                return findNode(node.left,key)
            else:
                return findNode(node.right,key)
        
        parent = findNode(root,key)

        deleteNode = parent.left if parent.left.val == key else parent.right

        replacement = deleteNode.right
        smallerNodes = deleteNode.left

        smallest = replacement
        while smallest.left:
            smallest = smallest.left
        
        smallest.left =smallerNodes

        if parent.left.val == key :
            parent.left = replacement
        else:
            parent.right = replacement
        
        return root



            