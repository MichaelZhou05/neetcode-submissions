class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #make 2d array dp where dp[i][j] represents number of ways
        # thus at a new position d[i][j] # of paths = d[i+1][j] + dp[i][j+1]

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1
        print(dp)

        for i in range(m):
            dp[i][n-1] = 1
        for j in range(n):
            dp[m-1][j] = 1
        

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
            
        print(dp)
        return dp[0][0]
