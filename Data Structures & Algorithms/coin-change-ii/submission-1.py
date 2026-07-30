class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 4
        dp =[[0]*len(coins) for _ in range(amount+1)]
        dp[0] = [1] * len(coins)

        for r in range(1,amount+1):
            for c in range(len(coins)):                

                dp[r][c] += dp[r-coins[c]][c] if r-coins[c] >= 0 else 0
                dp[r][c] += dp[r][c-1] if c-1 >=0 else 0



        return dp[-1][-1]


        #   1 2 3
        # 0 1 1 1
        # 1 1 0 0 
        # 2 1 1 0
        # 3 1 1 1  
        # 4 1 2 1


        #   1 2 3
        # 0 1 1 1
        # 1 1 1 1 
        # 2 1 2 2
        # 3 1 2 3  
        # 4 1 3 4