class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(n):
                if not matrix[r][c]:
                    matrix[r][0] = 0  
                    matrix[0][c] = 0
        
        for r in range(1,m):
            if not matrix[r][0]:
                matrix[r] = [0] * n

        for c in range(1,n):
            if not matrix[0][c]:
                for r in range(m):
                    matrix[r][c] = 0
        
        if not matrix[0][0]:
            matrix[0] = [0] * n
            for r in range(m):
                matrix[r][0] = 0
