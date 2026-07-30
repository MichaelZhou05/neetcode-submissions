import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = { "+": operator.add, "-": operator.sub, "*" : operator.mul, "/" : operator.truediv }
        
        for val in tokens :
            if val not in ops :
                stack.append(int(val))
            else: 
                total = ops[val](stack.pop(),stack.pop())
                stack.append(total)
        

        return stack.pop()
            
