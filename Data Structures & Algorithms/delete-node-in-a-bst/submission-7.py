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

        if smallest:
            while smallest and smallest.left:
                smallest = smallest.left
            
            smallest.left =smallerNodes

        if parent:
            if parent.left and parent.left.val == key :
                if replacement: 
                    parent.left = replacement
                else:
                    parent.left = smallerNodes
            else:
                if replacement: 
                    parent.right = replacement
                else:
                    parent.right = smallerNodes
        else:
            if replacement: return replacement
            if smallerNodes: return smallerNodes
            return None



            