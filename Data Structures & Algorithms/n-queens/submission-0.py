import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []

        emptyBoard = [["#"] * n for i in range(n)]

        
        def dfs(row, board):
            if row >= n :
                ret.append(["".join(row) for row in board])
                return
            for c in range(n):
                if board[row][c] == '#' :
                    newBoard = copy.deepcopy(board)
                    mark(newBoard, row, c)
                    dfs(row+1, newBoard)


    
        def mark(board, r, c):
            i, j = r + 1, c + 1
            while i < n and j < n:
                board[i][j] = "."
                i += 1
                j += 1

            i, j = r + 1, c - 1
            while i < n and j >= 0:
                board[i][j] = "."
                i += 1
                j -= 1

            board[r] = ["."] * n
            for row in range(n):
                board[row][c] = "."
            board[r][c] = "Q"

        dfs(0,emptyBoard)
        return ret

    

            
            
            


            