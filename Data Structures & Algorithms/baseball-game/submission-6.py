class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i,val in enumerate(operations):
            if val == "C":
                stack = stack[:-1]
            elif val == "D":
                stack.append(stack[-1]*2)
            elif val == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(val))
            
        return sum(stack)