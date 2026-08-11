class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        words = set(wordDict)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        startIndex = [0]

        for i in range(n):
            for start in startIndex:
                if s[start:i+1] in words:
                    dp[start][i+1] = 1
                    startIndex.append(i+1)
        
        ret = []
        def dfs(str1,r):
            if r == n:
                nonlocal ret
                ret.append(str1[1::])
                return
            for c in range(n+1):
                if dp[r][c]:
                    dfs(str1 + " " + s[r:c], c)
        
        dfs("",0)

        return ret

        
       
        

