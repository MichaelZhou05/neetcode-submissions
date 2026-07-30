# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = fast = head


        for i in range(n+1) :
            if not fast :
                if head :
                    temp = head.next
                    head.next = None
                    return temp
                else: 
                    head = None
                    return head
                    
            fast = fast.next
        

        while fast :
            head = head.next
            fast = fast.next
        
        temp = head.next
        head.next = head.next.next
        temp.next = None
        return start