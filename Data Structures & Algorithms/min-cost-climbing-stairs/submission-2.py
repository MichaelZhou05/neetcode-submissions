class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dfs(index) :
            if index in (1,0) :
                return cost[index]
            
            if index in cache :
                return cache[index]
            
            cache[index] = cost[index] + min(dfs(index-1), dfs(index-2))
            return cache[index]
        
        n = len(cost)
        return min(dfs(n-1),dfs(n-2))