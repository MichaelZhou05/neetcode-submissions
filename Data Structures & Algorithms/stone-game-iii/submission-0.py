class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0 for _ in range(n+1)] 		
        # dp[i] = max someone can collect if they started at index i

        currTotal = 0
        for i in range(n-1, -1,-1):
            currTotal += stoneValue[i]

            dp[i] = currTotal - min(dp[min(i+1,n)], dp[min(i+2,n)], dp[min(i+3,n)])
        

        if dp[0] > currTotal /2:
            return "Alice"
        elif dp[0]< currTotal/2:
            return "Bob"
        else:
            return "Tie"
