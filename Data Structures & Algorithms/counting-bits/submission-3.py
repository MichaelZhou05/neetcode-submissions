class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0,1,1,2,1] 
        
        i = 4
        while len(ret) < n+1:
            if len(ret) == i*2:
                ret.append(1)
                i *= 2
                continue
            ret.append(ret[i] + ret[len(ret)-i])

        
        return ret if n>=4 else ret[:n+1]
