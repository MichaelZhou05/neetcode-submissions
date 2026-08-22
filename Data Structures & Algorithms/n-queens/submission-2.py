class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = [0] * n
        diag1, diag2 = [0]*(2*n-1),[0] * (2*n-1)  # / -> diag1 \ -> diag 2


        ret = []
        def dfs(queens,c,row, diag1, diag2, m):
            if m == 0:              #sucessful build out matrix and append
                nonlocal ret
                nonlocal n
                matrix = ['.'*n for _ in range(n)]
                for r1,c1 in queens:
                    matrix[r1] = matrix[r1][:c1] + 'Q' + matrix[r1][c1+1:]
                ret.append(matrix)
                return

            
            for r in range(n):
                if not row[r] and not diag1[r+c] and not diag2[r-c]:
                    # print(r,c)
                    # print(diag1)
                    row[r],diag1[r+c],diag2[r-c] = 1,1,1
                    queens.append([r,c])
                    dfs(queens,c+1,row,diag1,diag2,m-1)
                    queens.pop()
                    row[r],diag1[r+c],diag2[r-c] = 0,0,0
            
            return 
        
        dfs([],0,row,diag1,diag2,n)
        return ret

