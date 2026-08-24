class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n


        for r in range(n-1,-1,-1):
            for i in range(r+1):
                minPath = 0
                if r+1 < n:
                    minPath += min(dp[i], dp[i+1])
                dp[i] = triangle[r][i] + minPath

        return dp[0]