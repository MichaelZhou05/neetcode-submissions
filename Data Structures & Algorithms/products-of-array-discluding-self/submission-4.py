class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [nums[0]]
        for i in range(1,len(nums)):
            ret.append(nums[i] * ret[i-1])
        
        postFix = 1
        for i in range(len(nums)-1,0,-1):
            ret[i] = ret[i-1] * postFix
            postFix *= nums[i]
        
        ret[0] = postFix
        
        
        return ret