class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        answer = [0,0,1,2]
        for i in range(n+1):
            if i <= 3:
                dp[i] = answer[i]
            else:
                dp[i] = max(3*dp[i-3], 2*dp[i-2],3*(i-3),2*(i-2))
                
        print(dp)
        return dp[n]
