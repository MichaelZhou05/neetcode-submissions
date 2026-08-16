class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:


        ret = []
        for i in range(min(len(word1),len(word2))):
            ret.append(word1[i])
            ret.append(word2[i])
        

        if len(word1) > len(word2):
            ret.append(word1[len(word2):])
        

        if len(word2) > len(word1):
            ret.append(word2[len(word1):])
        
        return "".join(ret)