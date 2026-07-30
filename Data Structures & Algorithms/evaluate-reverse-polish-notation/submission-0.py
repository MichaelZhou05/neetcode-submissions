import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = { "+": operator.add, "-": operator.sub, "*" : operator.mul, "/" : operator.truediv }
        var1, var2 = tokens[0], tokens[1]
        opIndex = 2

        while opIndex < len(tokens) :
            var1 = ops[tokens[opIndex]](int(var1),int(var2))
            opIndex += 2
            if opIndex >= len(tokens) : return var1
            var2 = tokens[opIndex-1]
            
        return var1