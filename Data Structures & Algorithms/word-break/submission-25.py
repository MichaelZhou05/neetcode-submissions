class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)
        lengths = set(len(w) for w in wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for L in lengths:
                j = i - L
                if j >= 0 and dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[n]
                    
                        
                    
                



#  catsincar
#i     ^
#l ^
#rl^
#ri   ^     
# sincars
#       ^



# iterate left to right, check if front to current index is a word in dict
# if it is, break off (cut to current index)