class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[i] = # ways to get to i amnt

        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        
        #     0,1,2,3,4
        # m=0 0 0 0 0 0 
        # m=1 1 1 1 1 1
        # m=2 1 1 2 2
        # m=3

        for m in range(1,len(coins)+1):
            dp[m][0] = 1
        
        for m in range(1,len(coins)+1):
            for i in range(1,amount+1):
                if i-coins[m-1] >= 0:
                    dp[m][i] += dp[m][i-coins[m-1]]
                dp[m][i] += dp[m-1][i]
        
        return dp[-1][-1]


                

                    


