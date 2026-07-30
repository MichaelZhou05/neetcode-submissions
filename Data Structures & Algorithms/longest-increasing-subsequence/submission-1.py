class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = 1

        for i in range(len(nums)-2, -1, -1) :
            mx = 1
            for j in range(i+1,len(nums),1) :
                if nums[i] < nums[j] :
                    mx = max(mx, 1 + dp[j])
            
            dp[i] = mx
        
        return max(dp)
                
