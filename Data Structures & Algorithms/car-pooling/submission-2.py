class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap=[]
        people=0
        heapq.heapify(heap)
        for trip in trips:
            heapq.heappush(heap,(trip[1],trip[0]))
            heapq.heappush(heap,(trip[2],-trip[0]))
        while heap:
            val=heapq.heappop(heap)
            people+= val[1]
            if people> capacity:
                return False
        return True


        