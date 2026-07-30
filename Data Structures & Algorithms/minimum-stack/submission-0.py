class MinStack:

    def __init__(self):
        global stack 
        stack = []
        global minStack 
        minStack = []

    def push(self, val: int) -> None:
        stack.append(val)
        minStack.append(min(val, minStack[-1] if minStack else float('inf')))

    def pop(self) -> None:
        stack.pop()
        minStack.pop()
        

    def top(self) -> int:
        return stack[-1]

    def getMin(self) -> int:
        return minStack[-1]
