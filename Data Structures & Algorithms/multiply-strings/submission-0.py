class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        multiplier = 1
        firstNum = 0
        for i in range(len(num1)-1,-1,-1):
            firstNum += (ord(num1[i]) - ord('0')) * multiplier
            multiplier *= 10
        
        multiplier = 1
        secondNum = 0
        for i in range(len(num1)-1,-1,-1):
            secondNum += (ord(num2[i]) - ord('0')) * multiplier
            multiplier *= 10
        
        print(firstNum)
        print(secondNum)
        return str(firstNum * secondNum)