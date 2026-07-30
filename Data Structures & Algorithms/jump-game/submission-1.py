class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canReach = [False] * n
        index = n-1

        canReach[index] = True
        index -= 1

        while index >=0 :
            for i in range(nums[index]+1):
                if index+i < n and canReach[index+i] :
                    canReach[index] = True
            index -= 1
        
        print(canReach)
        
        return canReach[0]
