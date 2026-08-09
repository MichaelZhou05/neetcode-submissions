class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word2), len(word1)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]


        for r in range(1,m+1):
            for c in range(1,n+1):
                if r == c:
                    if word2[r-1] == word1[c-1]:
                        dp[r][c] = dp[r-1][c-1]
                    else:
                        dp[r][c] = dp[r-1][c-1] + 1
                elif c > r:
                    if word1[c-1] == word2[r-1]:
                        dp[r][c] = min(dp[r][c-1] + 1, dp[r-1][c-1])
                    else:
                        dp[r][c] = dp[r][c-1] + 1
                else:
                    if word1[c-1] == word2[r-1]:
                        dp[r][c] = min(dp[r][c-1] + 1, dp[r-1][c-1])
                    else:
                        dp[r][c] = dp[r-1][c] + 1
        
        print(dp)
        return dp[-1][-1]








       #       m  o  n  k  e  y  s
       #    m  0  1  2  3  4  5  6  
       #    o  1  0  1  2  3  4  5
       #    n  2  1  0  1  2  3  4
       #    e  3  2  1  1  
       #    y                
       




       #   n e a t c d e e
       #n  0 1 2 3 4 5 6 7
       #e  1 0 1 2 3 4 5 6
       #e  2 1   
       #t         
       #c           
       #o            
       #d
       #e


       # @ each location, we want to get max number of continus charaters using min # of changes

       # 
       # if char matches -> no op, [r-1][c-1] + 1
       # no match 3 options:
       #    1) insert -> column offset -= 1
       #    2) delete ->  column offset += 1
       #    3) replace -> [r-1][c-1] + 1, # ops + 