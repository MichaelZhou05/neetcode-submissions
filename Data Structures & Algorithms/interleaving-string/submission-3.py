class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #dp[i][j] = if s1[:i] and s2[:j] can interleave to make s3[:i+j]
        #         = curr char matches and sub string without curr char mathes

        if len(s1) + len(s2)  != len(s3):
            return False

        dp = [[False for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

        dp[0][0] = True
        for c in range(1,len(s1)+1):
            dp[0][c] = dp[0][c-1] and s1[c-1] == s3[c-1]
        print(dp[0])


        for r in range(1,len(s2)+1):
            nextChar = s2[r-1]
            for c in range(len(s1)+1):
                dp[r][c] = (nextChar == s3[r+c-1] and dp[r-1][c]) or (c>0 and dp[r][c-1] and s1[c-1] == s3[r+c-1])
        
        return dp[-1][-1]
