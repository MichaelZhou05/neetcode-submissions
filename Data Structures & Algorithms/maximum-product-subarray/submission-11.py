class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxV = float('-inf')

        dp = [[0,0]for _ in range(len(nums))]

        for i,arr in enumerate(dp):
            if i == 0:
                arr[0],arr[1] = nums[0],nums[0]
            else:
                currVal = nums[i]
                arr[0] = max(currVal,currVal * dp[i-1][0], currVal * dp[i-1][1])
                arr[1] = min(currVal,currVal * dp[i-1][0], currVal * dp[i-1][1])
                maxV = max(maxV,arr[0])

        return max(maxV,dp[-1][0])

            
         #-3,-2, -4,0
    #max  -3 2  8
    #min  -3 -2  


    # for list going left -> right
    # @ each index keep track of
    # 1. max subarray including current index
    # 2. min subarray including current index
    # thus the @ next index
    # max & min = itself not multi before
    # or itself multi by max before