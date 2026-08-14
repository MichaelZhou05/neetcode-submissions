class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        #dp[i][j] = # of distince subsquences for s[:i] mathces t[:j]
        # dp[i][j] 
        # if s[i] != t[j] no iontroduction of new subsquences --> dp[i][j] == dp[i-1][j]
        # if they do match dp[i-1][j] + dp[i-1][j-1]
        for r in range(len(s)+1):
            dp[r][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1] 
                else:
                    dp[i][j] = dp[i-1][j]
                

        print(dp)
        return dp[-1][-1]
