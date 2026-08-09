class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word2), len(word1)




       #       m   o    n    k    e    y    s
       #    m  1  ---------------------------
       #    o  x   2 ------------------------    
       #    n  x   x   3 -------------------  
       #    e  x   x   x    4|1  4|1  
       #    e                    

       #    y  x   x   x                   
       




       #   n e a t c d e e
       #n  1 
       #e    2
       #e   1  3|1
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