class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * (len(s) + 1)
        dp[-1] = True

        def dfs(index):
            if dp[index] != None:
                return dp[index]
            
            dp[index] = False
            for word in wordDict :
                temp = index + len(word)
                print(temp)
                if temp <= len(s) and s[index:temp] == word:
                    dp[index] = dp[index] or dfs(temp)
            
            return dp[index]
            

        dfs(0)
        print(dp)
        return dp[0]
                
                    
                
                



