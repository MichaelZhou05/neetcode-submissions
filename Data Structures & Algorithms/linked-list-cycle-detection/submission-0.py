# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s1 = set()

        while True:
            if not head:
                return False
            if head not in s1 :
                s1.add(head)
            else :
                return True
            
            head = head.next
            