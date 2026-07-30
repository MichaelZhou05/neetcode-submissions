class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[-1 for _ in range(len(matrix[0])+1)]for _ in range (len(matrix)+1)]
        self.prefix[0] = [0] * (len(matrix[0])+1)
        for r in range(len(matrix)+1):
            self.prefix[r][0] = 0
        
        n = len(matrix)+1
        m = len(matrix[0])+1
        for r in range(1,n):
            currRowPrefix = 0
            for c in range(1,m):
                self.prefix[r][c] = matrix[r-1][c-1] + self.prefix[r-1][c] + currRowPrefix
                currRowPrefix += matrix[r-1][c-1]
        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)