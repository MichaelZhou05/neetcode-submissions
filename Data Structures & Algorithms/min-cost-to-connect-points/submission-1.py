class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #construct graph of every node mahannen distance to other nodes

        adjList = defaultdict(list)

        for i,arri in enumerate(points):
            xi,yi = arri[0],arri[1]
            for j in range(i+1,len(points)):
                arrj = points[j]
                xj,yj = arrj[0],arrj[1]
                distance = abs(xj-xi) + abs(yj-yi)
                adjList[(xi,yi)].append([distance,xj,yj])
                adjList[(xj,yj)].append([distance,xi,yi])
        
        visited = set()
        hq = []
        heapq.heappush(hq,[0,points[0][0],points[0][1]])
        ret = 0
        while len(visited) < len(points):
            distance,x,y = heapq.heappop(hq)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            ret += distance
            for dis,xi,yi in adjList[(x,y)]:
                if (xi,yi) not in visited:
                    heapq.heappush(hq,[dis,xi,yi])
        
        return ret
            

