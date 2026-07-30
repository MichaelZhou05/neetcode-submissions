class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text2, text1 = text1, text2
        
        s = defaultdict(list) #char -> index

        for i,c in enumerate(text2):
            s[c].append(i)

        ret = 0
        recent = -1
        for char in text1:
            if char in s :
                for i,val in enumerate(s[char]) :
                    if val > recent:
                        ret += 1
                        recent = i 
        
            
        return ret
        

