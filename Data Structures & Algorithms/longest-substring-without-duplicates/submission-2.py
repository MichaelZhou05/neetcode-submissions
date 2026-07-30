class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s) : return 0
    

        length = 1
        l,r = 0, 1
        hs = set()
        hs.add(s[l])

        while r<len(s) :
            if s[r] not in hs :
                hs.add(s[r])
                length = max(length, r-l +1)
                r +=1 
            else :
                hs.clear()
                l+=1
                r=l+1
                hs.add(s[l])
        
        return length

