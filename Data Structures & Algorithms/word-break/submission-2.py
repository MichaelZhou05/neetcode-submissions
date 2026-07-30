class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * (len(s) + 1)
        dp[-1] = True

        def dfs(index):
            if dp[index] != None:
                return dp[index]
            
            for word in wordDict :
                temp = index + len(word)
                if s[index:temp] in wordDict:
                    dp[index] = dfs(temp)
                dp[index] = False or dp[index]
            
            return dp[index]
            

            
        return dfs(0)
                
                    
                
                



