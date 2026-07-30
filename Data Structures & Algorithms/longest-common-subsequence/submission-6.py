class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = int(text1[0] == text2[0])

        for j in range(1,n):
            dp[0][j] = int (dp[0][j-1] or text1[j] == text2[0])

        for i in range(1,m):
            dp[i][0] = int(dp[i-1][0] or text1[0] == text2[i])


        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + 1 if text2[i] == text1[j] else max(dp[i-1][j],dp[i][j-1])
        
        print(dp)
        return dp[-1][-1]

        #   b l
        #y  0 0 
        #b  1
        #y  