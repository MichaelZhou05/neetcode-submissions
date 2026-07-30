class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' : return 0
        dp = [1] * (len(s))
      
            
        for i in range(len(s)-1, -1, -1):
            if (s[i] == "0"):
                dp[i] = 0
            elif (i==len(s)-1):
                dp[i] = 1
            elif (int(s[i]+s[i+1]) > 26):
                dp[i] = dp[i+1]
            else :
                if (i+2>=len(s)):
                    dp[i] = dp[i+1] +1
                else:
                    dp[i] = dp[i+1] + dp[i+2]

        return dp[0]