import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = { "+": lambda x, y: x+y, "-": lambda x, y: x-y, "*" : lambda x, y: x*y, "/": lambda x, y: int(x / y) }
        
        for val in tokens :
            if val not in ops :
                stack.append(int(val))
            else: 
                var1 = stack.pop()
                var2 = stack.pop()
                total = ops[val](var2,var1)
                print(total)
                stack.append(total)
        

        return stack.pop()
            
