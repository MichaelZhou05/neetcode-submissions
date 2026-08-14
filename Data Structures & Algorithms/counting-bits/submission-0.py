class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0,1,1,2,1,] 
        for i in range(n+1):
            if i >= len(ret):
                ret.append(1+ret[i-4])
        
        return ret
