class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lSum = 0
        leftindex = 0
        for i,val in enumerate(nums):
            lSum += val
            if lSum < 0 :
                leftindex = i+1
        
        rSum = 0
        rightindex = len(nums)-1

        for i in range(len(nums)-1, -1, -1) :
            rSum += nums[i]
            if rSum < 0:
                rightindex = i-1
        
        print(leftindex)
        print(rightindex)

        if leftindex > rightindex:
            return max(nums)

        return sum(nums[leftindex:rightindex+1])
            
