class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        

        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]


        while(slow != fast) :
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        
        slow = 0
        while (slow != fast) :
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
