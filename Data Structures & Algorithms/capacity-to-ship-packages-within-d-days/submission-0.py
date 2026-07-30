class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCap,maxCap = max(weights), sum(weights)

        def isValidCap(cap) -> bool:
            day = 0 
            currWeight = 0
            for weight in weights:
                currWeight += weight
                if currWeight > cap:
                    day += 1
                    currWeight = weight
            day += 1
            return day<=days
        

        while minCap < maxCap:
            midCap = (minCap+maxCap)//2
            
            if isValidCap(midCap):
                maxCap = midCap -1
            else:
                minCap = midCap+1
        
        
        return minCap if isValidCap(minCap) else minCap+1