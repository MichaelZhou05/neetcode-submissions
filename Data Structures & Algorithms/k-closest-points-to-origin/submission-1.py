class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [[math.sqrt(arr[0]*arr[0] + arr[1]*arr[1]), arr[0], arr[1]] for arr in points]
        heapq.heapify(distance)

        ret = []
        for i in range(k) : 
            ls1 = heapq.heappop(distance)
            ret.append([ls1[1],ls1[2]])
        
        return ret
        

