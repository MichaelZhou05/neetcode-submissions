class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e27] * (amount +1)
        dp[0] = 0 

        for num in range(1, amount+1) :
            res = 1e27
            for x in coins: 
                left = num - x
                if left < 0 :
                    continue
                res = min(res, 1 + dp[left])
                dp[num] = res
            
        ret = dp[amount]
        return ret if ret < 1e27 else -1
            
                
                
