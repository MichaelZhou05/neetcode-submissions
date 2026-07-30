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
            
            l = dfs(index+1) 
            r = dfs(index+2) if index+2 < len(s) and int(s[index+1] + s[index+2]) < 27 else 0
            cache[index] = l+r
            return l+r
        
        if not dfs(0) :
            return 0 
        return cache[0] + cache[1] if 1 in cache else cache[0]

