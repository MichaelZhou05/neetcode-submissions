class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        

        def search(arr) :
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])
            
            return dp[-1]
        
       
        return max(search(nums[:-1]), search(nums[1:]), search(nums[2:] + nums[0:1]))
