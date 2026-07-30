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
            
            dp[index] = False if dp[index] == None else True
            
            return dp[index]
            

        dfs(0)
        print(dp)
        return dp[0]
                
                    
                
                



