class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0 for _ in range(n)] for _ in range(n)] # dp[r][i] = min path to bot of triangle


        for r in range(n-1,-1,-1):
            for i in range(r+1):
                if r+1 < n:
                    dp[r][i] += min(dp[r+1][i], dp[r+1][i+1])
                print(r)
                dp[r][i] += triangle[r][i]

        return dp[0][0]