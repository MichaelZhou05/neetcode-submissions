class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #       (0,0)
        #   right    down
        #  (0,1)     (1,0)

        m,n = len(obstacleGrid), len(obstacleGrid[0])

        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]


        dp[m-1][n-1] = 1

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r==m-1 and c==n-1: continue #skip base
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]

        print(dp)
        return dp[0][0]   