class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #dp[]

        nums = [1] + nums + [1]

        dp = [[None for _ in range(len(nums))] for _ in range(len(nums))]
        
        def dfs(l,r):
            if r<l:
                return 0
            if dp[l][r]:
                return dp[l][r]
            currMax = 0
            for i in range(l,r+1):
                left = dfs(l,i-1)
                right = dfs(i+1,r)
                currMax = max(currMax, nums[i] * nums[l-1] * nums[r+1]+ left + right)
            
            dp[l][r] = currMax
            return dp[l][r]
        
        return dfs(1,len(nums)-2)

