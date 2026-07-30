class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin, maxProf = prices[0],0

        currProf = 0

        for n in prices :
            if n < currMin :
                currMin = n
                currProf = 0
                continue
            currProf = n - currMin
            maxProf = max(currProf, maxProf)

        return maxProf