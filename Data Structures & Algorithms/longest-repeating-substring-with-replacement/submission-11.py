class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = [0] * 26
        freqChar = s[0]
        maxLen = 1
        l = 0
        for r,char in enumerate(s):
            charCount[ord(char)-ord('A')] += 1
            if charCount[ord(char)-ord('A')] > charCount[ord(freqChar)-ord('A')]:
                freqChar = char
            
            replacements = (r-l+1) - charCount[ord(freqChar)-ord('A')]
            while replacements > k:
                charCount[ord(s[l])-ord('A')] -= 1
                replacements -= int(s[l] == freqChar)
                l += 1
            
            maxLen = max(maxLen,r-l+1)
