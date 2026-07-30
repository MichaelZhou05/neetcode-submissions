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
            prev = rev
            rev = rev.next
        prev.next = None

        #reverse rev
        prev = None
        while rev :
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp

        rev = prev
        
        while rev:
            nxt = head.next
            head.next = rev
            revNxt = rev.next
            rev.next = nxt
            head = nxt
            rev = revNxt
        
            