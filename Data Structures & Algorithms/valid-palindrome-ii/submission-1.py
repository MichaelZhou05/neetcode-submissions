
# abbda
#     ^   

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1] == s:
            return True
        for i in range(len(s)-1):
            str1 = s[0:i] + s[i+1:]
            if str1[::-1] == str1:
                print(str1)
                return True
            
        
        s = s[0:len(s)]
        return s[::-1] == s