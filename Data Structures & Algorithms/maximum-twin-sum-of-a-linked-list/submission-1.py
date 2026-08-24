# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # 5 -> 4 -> 2 -> 1
        #           ^

        n=0
        pointer = head

        while pointer:
            n+=1
            pointer = pointer.next
        

        pointer = head
        i = 0
        while i < n/2-1:
            pointer = pointer.next
            i+=1
        end = pointer
        pointer = pointer.next
        end.next = None

        prev,curr,next = None,pointer,None
        secondHead = None
        while curr:
            secondHead = curr
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        maxTwinSum = 0
        while secondHead and head:
            maxTwinSum = max(maxTwinSum,secondHead.val + head.val)
            print(maxTwinSum)
            head = head.next
            secondHead = secondHead.next

        return maxTwinSum        

        


        # def dfs(i,node):
        #     if i == n/2-1:
        #         twin = node.next
        #         twinSum = node.val + twin.val
        #         return [twinSum,twin.next]
            
        #     twinSum, twin = dfs(i+1,node.next)
        #     currSum = node.val + twin.val
        #     return [max(twinSum,currSum),twin.next]
        
        return dfs(0,head)[0]

