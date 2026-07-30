class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = s[0]

        for index in range(0,len(s)-1,1) :
            i = 1
            while index+i < len(s) and index-i >= 0 and s[index+i] == s[index-i] :
                i += 1
            i -= 1

            if (2*i+1) > len(ret) :
                ret = s[index-i: index+i+1]
            
            l = index
            r = index + 1

            while l>=0 and r < len(s) and s[l] == s[r] :
                l -=1
                r += 1
            l += 1
            r -= 1

            print(l)
            print(r)

            if (r-l+1) > len(ret) :
                ret = s[l:r+1]
        

        return ret
        

        
            