class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busyRooms = [] # [endTime, room#]
        roomCount = [0 for _ in range(n)]

        for i in range(n):
            busyRooms.append([0,i])
        

        freeRooms = []
        heapq.heapify(meetings)
        heapq.heapify(busyRooms)
        heapq.heapify(freeRooms)
        while meetings:
            start,end = heapq.heappop(meetings)

            while len(busyRooms) and start >= busyRooms[0][0]: #free up all rooms up until currStart time
                endTime, roomNum = heapq.heappop(busyRooms)
                heapq.heappush(freeRooms, roomNum)
            
            if len(freeRooms): # if there are rooms free use it
                newRoom = heapq.heappop(freeRooms)
                heapq.heappush(busyRooms, [end,newRoom]) 
                roomCount[newRoom] += 1
            else:           # no rooms free, must wait
                nextEnd, nextRoom = heapq.heappop(busyRooms)
                diff = nextEnd - start
       
                heapq.heappush(busyRooms, [end+diff,nextRoom])
                roomCount[nextRoom] += 1
            
   
        maxVal = max(roomCount)
        return roomCount.index(maxVal)