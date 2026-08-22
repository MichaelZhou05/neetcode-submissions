class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #start @ 0,0
        # for 4 directions mark as discoverable -> push into next element to explore heap with weight == list[r][c]
        # while heap, heap.pop. Do until reached list[-1][-1] return the max thus far on the path

        m,n = len(grid),len(grid[0])
        directions = [[0,1], [1,0], [0,-1],[-1,0]]
        que = [[grid[0][0],[0,0]]]  #[wieght,[r,c]]
        visited = set()
        maxElevation = 0

        while que:
            weight,arr = heapq.heappop(que)
            r,c = arr[0], arr[1]
            maxElevation = max(maxElevation,weight)
            if r == m-1 and c == n-1:
                return maxElevation

            visited.add((r,c))

            for dr,dc in directions:
                if r+dr<m and r+dr >=0 and c+dc<n and c+dc >= 0 and (r+dr,c+dc) not in visited:
                    heapq.heappush(que,[grid[r+dr][c+dc],[r+dr,c+dc]])

        
        return -1