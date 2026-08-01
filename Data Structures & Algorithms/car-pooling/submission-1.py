class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        currPassenger = 0
        trips.sort(key = lambda x : x[1])
        hq = [[0,0]] #location, passenger
        for passengers, from_i, to_i in trips:
            while len(hq) > 0 and from_i >= hq[0][0]:
                currPassenger -= heapq.heappop(hq)[1]
            
            currPassenger += passengers
            heapq.heappush(hq,[to_i, passengers])
            if currPassenger > capacity:
                return False
        
        return True

        