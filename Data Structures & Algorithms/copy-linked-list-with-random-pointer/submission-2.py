"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(head.val, None, None) if head else None
        ret = newHead
        start = head
        map1 = {}
        map1[head] = newHead

        while head and head.next :
            head = head.next
            newHead.next = Node(head.val, None, None)
            newHead = newHead.next
            map1[head] = newHead
        

        while start: 
            rand = start.random
            if rand :
                map1[start].random = map1[rand]
            else : 
                map1[start].random = None
            start = start.next
        
        return ret