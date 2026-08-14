class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(n):
                if not matrix[r][c]:
                    for c1 in range(n):
                        if matrix[r][c1]:matrix[r][c1] = '*' 
                    for r1 in range(m):
                        if matrix[r1][c]: matrix[r1][c] = '*'        

    
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '*':
                    matrix[r][c] = 0