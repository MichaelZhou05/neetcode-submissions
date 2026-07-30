class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # edge case 2 corners can always reach both Pacific and Atlantic
        m,n = len(heights), len(heights[0])

        pacific, atlantic = set(),set()

        traverse = [[0,1],[1,0],[-1,0],[0,-1]]


        def dfs(row, col, s) :
            if row<0 or col<0 or row>=m or col >= n or (row,col) in s :
                return

            s.add((row,col))
            for rd,cd in traverse:
                r = row + rd
                c = col + cd
                if r>=0 and c>=0 and r<m and c < n and heights[r][c] > heights[row][col] and (r,c) not in s:
                    dfs(r,c,s)

        

        for c in range(n):
            dfs(0,c,pacific)
            dfs(m-1,c,atlantic)
        for r in range(m):
            dfs(r,0,pacific)
            dfs(r,n-1,atlantic)
        
        print(pacific)
        print(atlantic)
    
        return list(pacific&atlantic)
        
        
                



            