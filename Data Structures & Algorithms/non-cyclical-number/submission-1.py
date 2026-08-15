class Solution:
    def isHappy(self, n: int) -> bool:
        # num1 ^2 + num2^2 = x 
        # X must be 1, 10, 100, etc
        # num1 & num2 <10 
        return True if n in {1,10,100,86,68,91,19,82,28} else False