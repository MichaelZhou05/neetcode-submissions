class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text2, text1 = text1, text2
        
        s = set()
        
        for c in text2:
            s.add(c)

        ret = 0
        for char in text1:
            if char in s:
                ret += 1
        
        return ret
        

