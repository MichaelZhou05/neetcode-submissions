import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap) # [-2,-3,-6,-2,-4]

        while len(heap) > 1 :
            x,y = -heapq.heappop(heap), -heapq.heappop(heap)

            if x == y :
                continue
            else : 
                heapq.heappush(heap, -1 * (x-y))
        

        return -heapq.heappop(heap) if heap else 0 








