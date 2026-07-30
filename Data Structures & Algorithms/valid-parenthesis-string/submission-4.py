class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []

        for i,x in enumerate(s) :
            if x == '(' : 
                stack.append(i)
            elif x == ')':
                if stack : 
                    stack.pop(-1)
                elif stars : 
                    stars.pop(-1)
                else: 
                    return False
            
            elif x == '*' :
                stars.append(i)


        while stack : 
            if not stars or stars.pop(-1) < stack.pop(-1):
                return False
            
        return True
            