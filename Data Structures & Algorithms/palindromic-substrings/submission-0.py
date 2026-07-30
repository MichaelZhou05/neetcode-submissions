class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i,char in enumerate(s):
            count += 1
            l,r = i, i+1
            while r < len(s) and l >=0 and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            size = 1
            while i-size >=0 and i+size < len(s) and s[i-size] == s[i+size]:
                count+=1
                size+=1
            
        

        return count



            

            