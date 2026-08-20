class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #dp[]

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        for i in range(1,n-1):
            dp[i][i] = nums[i]

        for l in range(n-2,0    ,-1):
            for r in range(l,n-1):
                currMax = 0
                for i in range(l,r+1):
                    currMax = max(currMax, nums[i]*nums[l-1]*nums[r+1] + dp[l][i-1] + dp[i+1][r])
                dp[l][r] = currMax
        
        return dp[1][n-2]