class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)//2

        dp = [[0 for _ in range(target + 1)] for _ in range(len(stones))]
        dp[0] = [0 for _ in range(stones[0])] + [stones[0] for _ in range(stones[0], target+1)]
        for r in range(1, len(stones)):
            for c in range(target+1):
                if c-stones[r] >= 0:
                    dp[r][c] = max(dp[r-1][c-stones[r]]+stones[r], dp[r-1][c]) 
             

                else:
                    dp[r][c] = dp[r-1][c]
        
        
        return sum(stones) - 2*dp[-1][-1]



        #   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
        # 2 0 2 2 2 2 2 2 2 2 2  2  2  2  2  2  2     
        # 7 0 2 2 2 2 2 7 7 9 9  9  9  9  9  9  9
        # 4 0 2 2 4 4 6 7 
        # 1 1
        # 8 0 
        # 1 0