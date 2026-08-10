class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        val = 1
        for i in range(32):
            res = res | ((n & val)>> i) << (31-i)
            val = val << 1
        
        return res