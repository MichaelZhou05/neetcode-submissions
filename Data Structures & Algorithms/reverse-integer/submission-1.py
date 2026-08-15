class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = 2**31, 2**31-1

        ret = 0 
        negative = x<0
        if negative: x *= -1
        while x:
            nextVal = x%10
            x = x//10

            if not negative and ret > MAX//10 or (ret == MAX//10 and nextVal%10 > MAX%10):
                return 0
            if negative and ret > MIN//10 or (ret == MIN//10 and (nextVal%10)>MIN%10):
                return 0
            ret *= 10
            ret += nextVal
        
        return -1*ret if negative else ret