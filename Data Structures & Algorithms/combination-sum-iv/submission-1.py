class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #BRUTE FORCE
        # it takes x different num to get to > target
        # each time we can chose any num in array
        # stop if we go above target

        # go by increasing target:
        # start @1 -> 1 way
        #  @2 -> 2 ways
        #  @3 -> 4
        #  @4 -> 1 + 4 + 2 = 7
        

        dp = [0 for _ in range(target+1)] #index -> sum  | val -> ways
        dp[0] = 1

        for i in range(len(dp)):
            for num in nums:
                if i-num >= 0 :
                    dp[i] += dp[i-num]



        return dp[-1]


