class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [0] * (len(nums)+1)
        for i in range(2,len(nums)+1,1):
            dp1[i] = max((nums[i-2]+dp1[i-2]),dp1[i-1])
        
        dp2 = [0] * (len(nums)+2)
        for i in range(3,len(nums)+2,1):
            dp2[i] = max((nums[i-2]+dp2[i-2]),dp2[i-1])

        return max(dp2[-1],dp1[-1])



