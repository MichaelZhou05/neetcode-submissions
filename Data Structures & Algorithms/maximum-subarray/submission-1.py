class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        leftindex = 0
        for i,val in enumerate(nums):
            if i > 0 :
                if nums[i] + nums[i-1] < 0 :
                    leftindex = i+1
                else:
                    break
        
        rightindex = len(nums)-1

        for i in range(len(nums)-1, -1, -1) :
            if i < len(nums)-1:
                if nums[i+1] + nums[i] < 0:
                    rightindex = i-1
                else: 
                    break
        
        print(leftindex)
        print(rightindex)

        if leftindex > rightindex:
            return max(nums)

        return sum(nums[leftindex:rightindex+1])
            
