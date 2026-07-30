"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp1 = {}
        que = []

        if node:
            que.append(node)

        while len(que):
            n = que.pop()
            temp = Node(n.val)
            mp1[n] = temp

            for x in n.neighbors :
                if x not in mp1:
                    que.append(x)
        
        for n in mp1 :
            copy = mp1[n]
            ls1 = []

            for x in n.neighbors :
                ls1.append(mp1[x])
            
            copy.neighbors = ls1
        

        return mp1[node] if len(mp1) else None

            