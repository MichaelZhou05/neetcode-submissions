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
            
            dp[i] = minV + 1 if (minV != float('inf') and minV != -1) else -1

        return dp[-1]


        # let i = amount
        # let dp[i] = min # of coins to get amount i 
        # 0 1 2 3 4 5 6 7 8 9 10 11 12
        # 0 1 2 3 4 1     

        # 0 1 2 3
        # -1  1 


        # at each index dp = min of i- all elements in coins + 1