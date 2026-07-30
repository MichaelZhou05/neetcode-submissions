class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def search(r,c):
            if r<0 or c<0 or r>=len(grid) or c >= len(grid[0]) or grid[r][c]=="0":
                return
            
            grid[r][c] = "0"
            search(r+1,c)
            search(r,c+1)
            search(r-1,c)
            search(r,c-1)

        for row in range(len(grid)) :
            for col in range(len(grid[0])):
                if grid[row][col] == "1" :
                    search(row,col)
                    count += 1
        

        return count

      
        
