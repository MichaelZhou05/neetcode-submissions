class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' : return 0
        dp = [1] * (len(s) + 1)
        # 1312

        #can be split
        #   num of ways 
        #cannot be split
        #   1
            
        for i in range(len(s)-2, -1, -1):
            if (int(s[i]+s[i+1]) > 26):
                dp[i] = dp[i+1]
            elif (s[i] == "0"):
                dp[i] = 0
            else :
                dp[i] = dp[i+1] + dp[i+2]

        return dp[0]