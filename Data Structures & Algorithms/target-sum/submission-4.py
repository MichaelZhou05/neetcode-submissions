class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        dp = [[0 for _ in range(2*total+1)] for _ in range(len(nums))] # 0 @ total/2
        
        zero = (2*total+1)//2
        dp[0][zero+nums[0]] += 1
        dp[0][zero-nums[0]] += 1

        for i in range(1,len(nums)):
            for j in range(len(dp[0])):
                if dp[i-1][j]:
                    if j+nums[i] < len(dp[0]): dp[i][j+nums[i]] += dp[i-1][j]
                    if j-nums[i] >= 0: dp[i][j-nums[i]] += dp[i-1][j]
        
        return dp[-1][zero + target] if zero+target < len(dp[0]) else 0