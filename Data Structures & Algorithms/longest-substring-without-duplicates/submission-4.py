class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        length = 0
        chars = set()
        for c in s:
            chars.add(c)
            length += 1
            if length != len(chars):
                length = 1
                chars  = set(c)
            maxLength = max(length,maxLength)
        
        return maxLength



