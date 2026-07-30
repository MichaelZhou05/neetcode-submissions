import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isFast(k: int) -> bool:
            counter = 0 
            for n in piles :
                counter += math.ceil(n/k)
            return True if counter <= h else False
            
        
        
        maxSpeed, minSpeed = max(piles), 1
        
        while minSpeed <= maxSpeed :
            mid = (maxSpeed + minSpeed)//2
            if isFast(mid) :
                maxSpeed = mid-1
            else :
                minSpeed = mid+1
        
        return minSpeed


