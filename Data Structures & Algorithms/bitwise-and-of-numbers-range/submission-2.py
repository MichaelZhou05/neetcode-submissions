class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if right == left:
            return right
        return left & right >> (right-left).bit_length() << (right-left).bit_length()