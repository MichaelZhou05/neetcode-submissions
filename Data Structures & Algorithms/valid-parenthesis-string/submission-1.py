class Solution:
    def checkValidString(self, s: str) -> bool:
        diff = 0
        star = 0
        for x in s: 
            if x == '(' :
                diff += 1
            elif x == ')' :
                diff -= 1
            elif x == '*' :
                star += 1
            
            if diff + star < 0 :
                return False
            
        
        return abs(diff) <= star
