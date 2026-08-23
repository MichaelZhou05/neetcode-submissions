class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0], [0,-1],[-1,0]]
        m,n = len(grid),len(grid[0])

        fresh = 0
        rottenQue = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2: rottenQue.append([r,c])
                elif grid[r][c] == 1: fresh +=1
        
        minute = -1
        visited = set()
        while rottenQue:
            minute += 1
            nextQue = []
            for r,c in rottenQue:
                visited.add((r,c))
                for dr,dc in directions:
                    if r+dr>=0 and r+dr<m and c+dc >=0 and c+dc<n and grid[r+dr][c+dc]==1 and (r+dr,c+dc) not in visited:
                        fresh -= 1
                        visited.add((r+dr,c+dc))
                        nextQue.append([r+dr,c+dc])
            
            rottenQue = nextQue
        
        print(fresh)
        return minute if not fresh else -1


