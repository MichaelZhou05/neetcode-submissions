class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])

        def bfs(r, c, d) :
            if r < 0 or c < 0 or r >= m or c >= n  or grid[r][c] == -1 or grid[r][c] < d:
                return
            
            grid[r][c] = min(grid[r][c], d)
            que.extend([[r+1,c,d+1],[r,c+1,d+1],[r-1,c,d+1],[r,c-1,d+1]])

        que = []
        for row in range(m) :
            for col in range(n):
                if grid[row][col] == 0 :
                    que.extend([[row+1,col,1],[row,col+1,1],[row-1,col,1],[row,col-1,1]])

        while len(que):
            r,c,distance = que.pop()
            bfs(r,c,distance)

            
