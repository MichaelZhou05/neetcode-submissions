class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s) : return 0
    

        length = 1
        l = 0 
        hm ={}

        for i,n in enumerate(s) :
            if n not in hm :
                hm[n] = i
                length = max(length, i-l + 1)
            else :
                nl = hm[n] +1
                while l<nl :
                    hm.pop(s[l])
                    l += 1
                hm[n] = i
            
        
        return length



