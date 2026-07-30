class Solution:
    def checkValidString(self, s: str) -> bool:
        diff = 0
        star = 0
        for x in s: 
            if x == '(' :
                diff += 1
            elif x == ')' :
                diff -= 1
            if x == '*' and diff > 0:
                star += 1
            if diff < 0 :
                if star > 0 :
                    star -= 1
                    diff += 1
                else:
                    return False
            
        
        return diff <= star
