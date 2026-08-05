class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(p), len(s)
        dp = [[None for _ in range(n+1)] for _ in range(m+1)]

        for c in range(n):
            dp[-1][c] = False
        
        dp[-1][-1] = True

        for r in range(m-1,-1,-1):
            if p[r] == '*':
                continue
            elif r+1< m and p[r+1] == '*':
                dp[r][-1] = dp[r+2][-1]
            else:
                dp[r][-1] = False




        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if dp[r][c]: continue
                if p[r] == "*" : continue
                
                if r+1 < m and p[r+1] == '*':
                    dp[r][c] = dp[r][c+1] or dp[r+2][c]
                
                else: 
                    dp[r][c] = (s[c] == p[r] or p[r] == '.') and dp[r+1][c+1]


        print(dp)

        return dp[0][0]