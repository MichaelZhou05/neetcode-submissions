class Solution:
    def climbStairs(self, n: int) -> int:
        cach = {} #currentstep -> number of ways

        def dfs(step) -> int :
            if step == n:
                return 1
            if step > n : 
                return 0
            
            if step in cach :
                return cach[step]

            cach[step] = dfs(step+1) + dfs(step+2) 
            return cach[step]
        
        return dfs(0)