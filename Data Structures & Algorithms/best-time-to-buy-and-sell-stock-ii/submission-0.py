class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i,price in enumerate(prices):
            if i-1 >= 0 and price > prices[i-1]:
                profit += price - prices[i-1]
        

        return profit