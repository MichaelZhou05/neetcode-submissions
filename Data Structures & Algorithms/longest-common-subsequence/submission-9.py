class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
         # crabt
        #c 11111
        #a 11222
        #t 11223



        # xxxacbd
        #c    111
        #b    122
        #d    123
        #d    12


        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for r in range(1,len(text1)+1):
            for c in range(1,len(text2)+1):
                dp[r][c] = max(dp[r-1][c],dp[r][c-1],dp[r-1][c-1]+int(text1[r-1]==text2[c-1]))
        
        # print(dp)
        return dp[-1][-1]