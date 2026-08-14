class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0,1,1,2,1] 
        for i in range(5,n+1):
                ret.append(1+ret[i-4])
        
        return ret if n>=4 else ret[:n]
