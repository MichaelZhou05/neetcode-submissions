class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #build adjList
        adjList = defaultdict(list)
        for from_i, to_i, price_i in flights:
            adjList[from_i].append([to_i,price_i])
        
        hq =[]
        heapq.heappush(hq,[0,k,src])
        minPrice = float('inf')
        while hq:
            currCost,stops,node = heapq.heappop(hq)
          

            if node == dst:
                minPrice = min(minPrice,currCost)
                continue
            if stops < 0 :
                continue
            for nextNode in adjList[node]:
                heapq.heappush(hq,[currCost+nextNode[1],stops-1,nextNode[0]])

            
        return minPrice if minPrice != float('inf') else -1
