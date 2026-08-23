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
            while l<r and replacements > k:
                charCount[ord(s[l])-ord('A')] -= 1
                for i in range(26):
                    if charCount[i] > charCount[ord(freqChar)-ord('A')]:
                        freqChar = chr(i+ord('A'))
                replacements -= int(s[l] != freqChar)
                l += 1
            
            
            maxLen = max(maxLen,r-l+1)
        

        return maxLen
