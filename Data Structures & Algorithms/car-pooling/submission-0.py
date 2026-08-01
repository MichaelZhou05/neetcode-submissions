class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        currPassenger = 0
        trips.sort(key = lambda x : x[1])
        endTrips = [[0,0]] #location, passenger
        for passengers, from_i, to_i in trips:
            while len(endTrips) > 0 and from_i >= endTrips[0][0]:
                currPassenger -= endTrips.pop(0)[1]
            
            currPassenger += passengers
            endTrips.append([to_i, passengers])
            if currPassenger > capacity:
                return False
        
        return True

        