class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        #       3   Alice  t=4
        #      i=1         i=2
        #Bob  i=2   i=3    i=3,4
        #A  i=3,i=4  i=4      
        
        
        #  0 1 2 3 4 
        # [3,1,2,5,7]
        #    ^    
        # M=2 

        #optimal @ [i][M]
        #take X piles such that [i+X][max(M, 2X)] is not greater than the pile  you took
        
        # dp[i][j] = how much many stones you can optimally get total starting here
        # thus want to minimmize how many stones the other person gets
        #   [3,1,2,5,7]
        # 1  10 8 7 12 7 0      
        # 2  18 15 14 12 7 0
        # 3
        
        n = len(piles)

        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]


        totalStones = 0
        for i in range(n-1,-1,-1):
            totalStones += piles[i]
            for M in range(1,n):
                myBest = 0
                for X in range(1,2*M+1):
                    if i+X >= n+1: break
                    if X<n and totalStones - dp[max(M,X)][i+X] > myBest:
                        myBest = totalStones - dp[max(M,X)][i+X]
                        dp[M][i] = myBest

        return dp[1][0]