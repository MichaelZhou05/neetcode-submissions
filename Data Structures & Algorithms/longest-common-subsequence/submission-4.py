class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            dp[0][j] = 1 if text1[0] == text2[0] else 0

        for i in range(m):
            dp[i][0] = 1 if text1[0] == text2[0] else 0


        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + 1 if text2[i] == text1[j] else max(dp[i-1][j],dp[i][j-1])
        
        print(dp)
        return dp[-1][-1]

        #   c r a b t 
        #c  1 1 1 1 1 
        #a  1 1 2 2 2
        #t  1 1 