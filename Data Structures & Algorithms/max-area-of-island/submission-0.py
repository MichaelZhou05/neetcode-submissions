class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0

        def search(r,c) -> int:
            if r<0 or c<0 or r>=len(grid) or c >= len(grid[0]) or grid[r][c]=="0":
                return 0
            
            grid[r][c] = "0"
            return 1 + search(r+1,c) + search(r,c+1) + search(r-1,c) + search(r,c-1)

        for row in range(len(grid)) :
            for col in range(len(grid[0])):
                if grid[row][col] == "1" :
                    area = max(search(row,col), area)

        
        return area
                    
        
