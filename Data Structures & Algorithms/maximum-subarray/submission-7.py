class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currSum = 0
        ret = -1

        i = 0
        while i < len(nums):
            currSum += nums[i]
            if currSum < 0 :
                currSum = 0
                i += 1
                continue
            ret = max(ret, currSum)
            i += 1
    
        
        return ret

        
            
