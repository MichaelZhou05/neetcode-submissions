class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 0001010
        # 0001011
        # 0001100
        # 0001101
        
        # 001
        # 010
        # 011
        # 100
        # 101
        if right == left:
            return right
        return left & right >> (right-left).bit_length() << (right-left).bit_length()