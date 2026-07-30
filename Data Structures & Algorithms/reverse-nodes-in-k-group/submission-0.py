# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = head
        curr = head.next
        tail = head

        temp = prev
        for i in range(k-1) :
            temp = temp.next
            if not temp : return head
        newHead = temp.next
        head = temp


        while prev and curr :
            for i in range(k-1) :
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            tail.next = newHead
            prev = newHead
            curr = newHead.next if newHead else None
            
            temp = prev
            for i in range(k-1) :
                temp = temp.next if temp else None
                if not temp : return head
            newHead = temp.next
            tail.next = temp
            tail = prev

        return head