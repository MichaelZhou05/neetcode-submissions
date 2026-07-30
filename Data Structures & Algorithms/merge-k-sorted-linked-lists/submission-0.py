# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or not len(lists) :
            return None
        merge = lists
        while len(merge) > 1: 
            newMerge = []
            for i in range(0,len(merge), 2) :
                l1 = merge[i]
                l2 = merge[i+1] if i+1 < len(merge) else None
                newMerge.append(self.mergeit(l1,l2))
            merge = newMerge
                
        
        return merge[0]
        
    def mergeit(self, ls1, ls2) -> ListNode :
        if not ls2 :
            return ls1
        
        if ls2.val < ls1.val :
            temp = ls1
            ls1 = ls2
            ls2 = temp
        
        head = ls1

        while ls1 and ls2:
            if not ls1.next :
                ls1.next = ls2
                return head
            if ls2.val < ls1.next.val :
                temp = ls1.next
                ls1.next = ls2
                ls2 = ls2.next
                ls1 = ls1.next
                ls1.next = temp
            else :
                ls1 = ls1.next
            
        return head


           

        
        