class Solution:
    def solve(self, board: List[List[str]]) -> None:
        notSurrounded = set()
        m,n = len(board), len(board[0])

        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(r,c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            
            if board[r][c] == "O" and (r,c) not in notSurrounded:
                notSurrounded.add((r,c))
                for i,j in directions :
                    dfs(r+i,c+j)
        

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        
        for i in range(n):
            dfs(0,i)
            dfs(m-1, i)

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r,c) not in notSurrounded :
                    print((r,c))
                    board[r][c] = "X"
        
        print(notSurrounded)
            
 