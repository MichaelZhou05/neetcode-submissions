class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        l,r = 1,x
        while l<=r:
            mid = (l+r)//2
            squared = mid * mid
            if squared == x:
                return mid
            if squared > x:
                r = mid - 1
            else:
                l = mid + 1
         
            
        
        return l if (l * l) < x else l-1
