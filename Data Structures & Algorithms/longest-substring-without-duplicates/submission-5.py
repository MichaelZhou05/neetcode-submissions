class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        length = 0
        chars = set()
        lastIndex = 0
        for c in s:
            chars.add(c)
            length += 1
            if length != len(chars):
                while s[lastIndex] != c:
                    chars.remove(s[lastIndex])
                    lastIndex += 1
                    length -=1
                lastIndex +=1
                length -=1
                



            maxLength = max(length,maxLength)
        
        return maxLength



