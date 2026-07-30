class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = 0
        resetL = -1
        maxLength = max(len(s) for s in wordDict)
        for i in range(len(s)):
            currStr = s[l:i+1]
            if i+1 - l > maxLength:
                if l == resetL: #been reset before
                    return False
                l =resetL
                i = resti
            if currStr in wordDict:
                resestL = l
                reseti = i
                l = i+1
        
        return l >= i


                
                    
                
                



#  catsincar
#i     ^
#l ^
#rl^
#ri   ^     
# sincars
#       ^



# iterate left to right, check if front to current index is a word in dict
# if it is, break off (cut to current index)