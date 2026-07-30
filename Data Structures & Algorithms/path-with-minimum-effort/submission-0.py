class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set()
        n = len(heights)
        m = len(heights[0])

        #minEffort to get to each position
        minEffort = [[0 for _ in range(m)]for _ in range(n)] 

        #unvisted nodes and curr minEffort to reach
        hq = [] 
        heapq.heappush(hq,[0,0,0]) 

        while hq:
            currMinEffort, r,c = heapq.heappop(hq)
            if (r,c) == (n-1,m-1):
                return currMinEffort
            if (r,c) in visited : continue
            if r+1 < n :
                if abs(heights[r+1][c]-heights[r][c]) > currMinEffort:
                    newEff = abs(heights[r+1][c]-heights[r][c])
                    heapq.heappush(hq,[newEff,r+1,c])
                else:
                    heapq.heappush(hq,[currMinEffort,r+1,c])
            if r-1 >= 0 :
                if abs(heights[r-1][c]-heights[r][c]) > currMinEffort :
                    newEff = abs(heights[r-1][c]-heights[r][c])
                    heapq.heappush(hq,[newEff,r-1,c])
                else:
                    heapq.heappush(hq,[currMinEffort,r-1,c])
            if c+1 < m :
                if abs(heights[r][c+1]- heights[r][c])> currMinEffort:
                    newEff = abs(heights[r][c+1]-heights[r][c])
                    heapq.heappush(hq,[newEff,r,c+1])
                else:
                    heapq.heappush(hq,[currMinEffort,r,c+1])
            if c-1 >= 0 :
                if abs(heights[r][c-1]-heights[r][c]) > currMinEffort:
                    newEff = abs(heights[r][c-1]-heights[r][c])
                    heapq.heappush(hq,[newEff,r,c-1])
                else: 
                    heapq.heappush(hq,[currMinEffort,r,c-1])
            visited.add((r,c))
                
            
        return -1
            



        #first construct graph with nodes and path

        

        #
        #   [0,0,0],
        #   [2,1,3],
        #   [1,4,3]
 
        #  at each cell the mmin effort = min(effort comming from up,down left or right)
        # min effrot coming from a direction = max(diff curr height last cell height, min effort to last cell)

        #
        #
