
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        ret = 0
        n,m = len(grid),len(grid[0])
        for r in range(n):
            for c in range(m):
                if grid[r][c] :
                    ret += 4
                    for dr,dc in directions:
                        ret -= grid[r+dr][c+dc] if r+dr >= 0 and r+dr < n and c+dc >= 0 and c+dc < m else 0 
        

        return ret