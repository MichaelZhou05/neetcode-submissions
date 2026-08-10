class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
       # find max subarray 
        total = sum(nums)
        
        maxVal = 0
        currVal = 0
        for i,val in enumerate(nums):
            currVal += val
            if currVal <= 0:
                currVal = 0
            maxVal = max(maxVal,currVal)
        
        minVal = 0
        currVal = 0
        for val in nums:
            currVal += val
            if currVal >= 0:
                currVal = 0
            minVal = min(minVal,currVal)

        return max(maxVal, total-minVal)

        
