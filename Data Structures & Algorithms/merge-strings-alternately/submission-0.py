class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word2) > len(word1): word1,word2 = word2,word1


        ret = []
        for i in range(len(word2)):
            ret.append(word1[i])
            ret.append(word2[i])
        

        if len(word1) > len(word2):
            ret.append(word1[len(word2):])
        
        return "".join(ret)