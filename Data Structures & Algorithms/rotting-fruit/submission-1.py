class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        maxTime = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        que = []

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2 :
                    que.append([r,c,0])

        
        while que :
            r,c,t = que.pop(0)
            if t>maxTime :
                maxTime = t
            grid[r][c] = 2

            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if nr>=0 and nr<m and nc >=0 and nc< n and grid[nr][nc] == 1 :
                    que.append([nr,nc,t+1])
            


        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 :
                    return -1
        
        return maxTime

            