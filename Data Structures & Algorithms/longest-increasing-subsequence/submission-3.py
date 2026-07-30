class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp =[[-1,-1] for _ in range(len(nums))]
        dp[0][0],dp[0][1] = 1,nums[0]

        count = 1

        #at every index dp[i][0] = current count, dp[i][1] = curr Max 
        for i,val in enumerate(nums):
            for j in range(i):
                if val > dp[j][1] and dp[j][0]+1 > dp[i][0]:
                    dp[i][0] = dp[j][0]+1
                    count = max(count,dp[i][0])
                    dp[i][1] = val
            
            if dp[i][0] == -1 and dp[i][1] == -1:
                dp[i][0], dp[i][1] = 1, val
        

        return count
            
        

                

                
