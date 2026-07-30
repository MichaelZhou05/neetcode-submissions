class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [1,2,1,2,1,1|0 0]
        #【4 5 3 3 2 1 1， 0
        #   

        dp = [0] * (len(cost)+2)
        print(dp)

        for i in range(len(cost)-1,-1,-1):
            dp[i] = cost[i] + min(dp[i+1],dp[i+2])
        
        return min(dp[1],dp[0])
                 