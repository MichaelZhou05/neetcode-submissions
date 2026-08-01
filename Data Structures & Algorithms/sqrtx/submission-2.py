class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        l,r = 1,x
        mid = None
        while l<r:
            mid = (l+r)//2
            squared = mid * mid
            if squared == x:
                return mid
            if squared > x:
                r = mid - 1
            else:
                l = mid + 1
            
        
        return l if mid * mid < x else l-1
