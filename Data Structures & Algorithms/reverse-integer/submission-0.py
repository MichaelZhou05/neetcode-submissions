class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -1* 2**31, 2**31-1

        ret = 0 
        negative = x<0
        if negative: x *= -1
        while x:
            ret *= 10
            ret += x%10
            x = x//10

            if ret > MAX//10 or (ret == MAX//10 and x%10 > MAX%10):
                return 0
            if negative and -1*ret < MIN//10 or (-1*ret == MIN//10 and -1*(x%10)<MIN%10):
                return 0
        
        return -1*ret if negative else ret