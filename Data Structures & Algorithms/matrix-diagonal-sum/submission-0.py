class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ret = 0 
        n = len(mat)
        for i in range(n):
            ret += mat[i][i]
            if n-1-i != i:
                ret += mat[i][n-1-i]
        
        return ret