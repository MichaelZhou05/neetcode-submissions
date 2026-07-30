class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(price) <= 1 return 0

        #
        #keep track of sell and don't sell @ index
        # in ideal world
        # buy if next day price ^
        # sell if next day price v
        # when price dips, you have 2 option
        # sell the day before & buy the next
        # sell today & don't buy tmrw

        #profit
        # 0 2 3 3 4 
        # 0 2 3 2 6

        #1,3,4,0,4,6



        #lp
        # 1 1 1 
        # 1 1 1


        dp = [-1] * len(prices)
        dp[0] = 0

        maxVal = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                dp[i] = prices[i] - prices[i-1] + dp[i-1]
            elif i+1 < len(prices):
                dp[i] = dp[i-1] - min(prices[i-1] - prices[i-2], prices[i+1]-prices[i])
            maxVal=max(maxVal,dp[i])

        print(dp)
        return maxVal