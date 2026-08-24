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
        

        def dfs(i,node):
            if i == n/2-1:
                twin = node.next
                twinSum = node.val + twin.val
                return [twinSum,twin.next]
            
            twinSum, twin = dfs(i+1,node.next)
            currSum = node.val + twin.val
            return [max(twinSum,currSum),twin.next]
        
        return dfs(0,head)[0]

