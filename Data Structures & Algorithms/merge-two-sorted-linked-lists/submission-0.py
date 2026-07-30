# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 : return list2
        if not list2 : return list1
        
        l1 = list1 if list1.val < list2.val else list2
        l2 = list2 if list1.val < list2.val else list1
    
        head = l1
        
        while l1 and l2:
            if l2.val < l1.next.val :
                temp = l1.next
                l1.next = l2
                l2 = l2.next
                l1 = l1.next 
                l1.next = temp
            else:
                l1 = l1.next
        
        return head
