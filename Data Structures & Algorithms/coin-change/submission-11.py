class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 : return 0
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0 

        for i in range(1,amount+1):
            minV = float('inf')
            for val in coins:
                if i-val >= 0 and dp[i-val] != -1:
                    minV = min(dp[i-val],minV) 
            
            dp[i] = minV + 1 if minV < 99999 else -1

        return dp[-1]


