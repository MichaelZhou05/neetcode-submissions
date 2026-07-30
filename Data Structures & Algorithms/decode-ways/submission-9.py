class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {} #index -> number of answers


        def dfs(index) :
            if index == len(s) :
                return 1
            if int(s[index]) == 0:
                return 0

            if index in cache :
                return cache[index]
            
            res = dfs(index + 1)

            # Two-digit
            if index + 1 < len(s) and 10 <= int(s[index:index + 2]) <= 26:
                res += dfs(index + 2)

            return res
        
        return dfs(0)

