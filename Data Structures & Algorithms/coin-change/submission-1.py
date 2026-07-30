class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = float("inf")
        coins.sort()
        cache = {}

        def dfs(value, index) :

            if value == amount : return 0

            if value in cache :
                    return cache[temp] #need to update cache

            localMin = float("inf")
            for i in range(index, -1, -1):
                temp = value + coins[i]
                if temp > amount : 
                    continue

                count = dfs(temp,i)
                if count < localMin :
                    localMin = count
                    cache[temp] = localMin
            
            return 1 + localMin
        
        ret = dfs(0,len(coins)-1)
        return ret if ret < 9999 else -1
                
