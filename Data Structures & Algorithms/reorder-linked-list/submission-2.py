# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ct = head
        length = 0
        while ct :
            ct = ct.next
            length += 1
        
        n = length//2
        rev = head
        for i in range(length-n) :
            rev = rev.next
    
        #reverse rev
        prev = None
        while rev :
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp

        rev = prev
        
        for i in range(n) :
            nxt = head.next
            head.next = rev
            revNxt = rev.next
            rev.next = nxt
            head = nxt
            rev = revNxt
        
        head.next = None
        
            