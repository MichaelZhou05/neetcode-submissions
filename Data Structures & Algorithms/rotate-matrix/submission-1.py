class Solution:
    def rotate(self, matrix: List[List[int]]) -> None: 
        n = len(matrix)
        l = n-1
        for i in range(n//2):
            for j in range(n-i*2-1):
                temp = matrix[0+i][0+i+j]
                matrix[0+i][0+i+j] = matrix[l-i-j][0+i]
                matrix[l-i-j][0+i] = matrix[l-i][l-i-j]
                matrix[l-i][l-i-j] = matrix[0+i+j][l-i]
                matrix[0+i+j][l-i] = temp
        